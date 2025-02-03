# NRF24L01-Based Image Transmission with ESP8266

This project enables **wireless image transmission** using an **ESP8266 + NRF24L01** setup. The image is **compressed, split into chunks, transmitted**, and then **reconstructed** on the receiver side.

---

## 📌 Features

- 📡 **Fast wireless transmission** using NRF24L01 (2Mbps)
- 📷 **Image compression & chunking** for efficient transfer
- ✅ **Error handling** to detect and recover from data loss
- 🖼️ **Live image reconstruction** using OpenCV & PIL
- 🚀 **Optimized for ESP8266 + NRF24L01 transceivers**

---

## 🔧 Hardware Requirements

- **ESP8266 NodeMCU** (Sender & Receiver)
- **NRF24L01** Wireless Modules
- **Computer** (to run Python scripts for encoding/decoding)
- **Jumper Wires & Power Source**

---

## 🛠️ Installation & Setup

### **1️⃣ Connect NRF24L01 to ESP8266**

| NRF24L01   | ESP8266 (Sender) | ESP8266 (Receiver) |
| ---------- | ---------------- | ------------------ |
| VCC (3.3V) | 3.3V             | 3.3V               |
| GND        | GND              | GND                |
| CE         | D4               | D4                 |
| CSN        | D2               | D2                 |
| SCK        | D5               | D5                 |
| MOSI       | D7               | D7                 |
| MISO       | D6               | D6                 |

### **2️⃣ Flash the ESP8266 with Sender & Receiver Code**

- **Upload** `sender.ino` to **ESP8266 (Sender)**
- **Upload** `receiver.ino` to **ESP8266 (Receiver)**

### **3️⃣ Install Python Dependencies**

Run the following command to install required libraries:

```bash
pip install pyserial opencv-python pillow numpy
```

### **4️⃣ Run the Python Scripts**

- **Sender Side:**

```bash
python sender.py
```

- **Receiver Side:**

```bash
python receiver.py
```

---

## 📜 Project Structure

```
📂 nrf24l01_image_transmission
│── 📜 sender.ino          # ESP8266 Sender Code
│── 📜 receiver.ino        # ESP8266 Receiver Code
│── 📜 sender.py           # Python Script for Sending Image
│── 📜 receiver.py         # Python Script for Receiving Image
│── 📜 README.md           # Project Documentation
```

---

## 📢 Troubleshooting

### **🔹 Image Not Received Properly?**

✅ Ensure **NRF24L01 modules are properly wired**\
✅ **Reduce baud rate** if experiencing data loss\
✅ Try **adding delay in transmission** (e.g., `time.sleep(0.01)`)\
✅ **Use external 3.3V power source** for NRF24L01

### **🔹 Getting 'Corrupted Data' Errors?**

✅ Ensure **all chunks are received & sorted before reconstruction**\
✅ **Enable CRC checks** to detect packet corruption

---

## 📜 License

This project is **open-source** under the MIT License.

---

## 💡 Future Improvements

- 🔄 **Implement retransmission for lost packets**
- 📡 **Improve transmission speed & efficiency**
- 🔍 **Use advanced compression (JPEG/WebP) for faster transfer**

---

## ⭐ Contributors

👨‍💻 **[Divyansh Yadav]** – Developer & Maintainer

👨‍💻 [Subham Kumar] (2nd Year IT Student at IIIT Una)

If you found this useful, give it a ⭐ on **GitHub**!

