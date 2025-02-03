#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>

#define CE_PIN D4  // D2 on ESP8266
#define CSN_PIN D2 // D8 on ESP8266

RF24 radio(CE_PIN, CSN_PIN);
const byte address[6] = "00001";  // NRF24L01 address

void setup() {
    Serial.begin(460800);
    radio.begin();
    radio.openWritingPipe(address);
    radio.setPALevel(RF24_PA_MAX);  // Reduce power consumption
    radio.setDataRate(RF24_2MBPS);
    radio.stopListening();  // Set as transmitter
}

void loop() {
    if (Serial.available()) {
        char chunk[32];  
        Serial.readBytes(chunk, 32);  // Read 32-byte chunk from serial
        bool success = radio.write(chunk, sizeof(chunk));

        if (success) {
            Serial.println("Chunk sent");
        } else {
            Serial.println("Failed to send");
        }

        delay(5);  // Small delay to avoid collision
    }
}
