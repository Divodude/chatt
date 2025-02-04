#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN D4  // D4 on ESP8266
#define CSN_PIN D2 // D2 on ESP8266

RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "00001";  
int totalChunks = 0;
bool receiving = false;

void setup() {
    Serial.begin(460800);
    radio.begin();
    radio.openReadingPipe(1, address);
    radio.setPALevel(RF24_PA_MAX);
    radio.setDataRate(RF24_2MBPS);
    radio.startListening();  
}

void loop() {
    if (radio.available()) {
        char chunk[32] = {0};
        radio.read(&chunk, sizeof(chunk));

        if (strncmp(chunk, "START", 5) == 0) {  
            totalChunks = (chunk[5] << 8) | chunk[6];
            receiving = true;
            Serial.print("START signal received. Expecting ");
            Serial.print(totalChunks);
            Serial.println(" chunks.");
            return;
        }

        if (strncmp(chunk, "END", 3) == 0) {  
            Serial.println("END signal received. Stopping...");
            receiving = false;
            return;
        }

        Serial.write(chunk, sizeof(chunk));  

        radio.stopListening();
        radio.write("ACK", 3);
        radio.startListening();
    }
}
