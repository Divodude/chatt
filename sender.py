import serial
import struct
import io
import time
from PIL import Image
baudrate =460800
ser = serial.Serial("COM5", baudrate, timeout=1)

def image_to_chunks(image_path, chunk_size=30):
    with Image.open(image_path) as img:
        img=img.resize((200,100))
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format="PNG")
        binary_data = img_byte_array.getvalue()

    chunks = []
    for i in range(0, len(binary_data), chunk_size):
        chunk_data = binary_data[i:i + chunk_size]
        chunk_index = struct.pack("H", i // chunk_size)  
        chunks.append(chunk_index + chunk_data.ljust(chunk_size, b'\x00')) 
    return len(chunks), chunks

def send_chunks(image_path):
    total_chunks, chunks = image_to_chunks(image_path)
    print(f"Sending {total_chunks} chunks...")

    ser.write(b'ST')  # Start signal
    ser.write(struct.pack("H", total_chunks))

    for chunk in chunks:
        ser.write(chunk) 
        time.sleep(0.025)

    ser.write(b'EN')  # End signal
    print("Transmission complete.")

send_chunks(r"C:\Users\Divyansh\mygallery\static\userimages\WhatsApp_Image_2024-09-08_at_23.54.06_6e3ea34c.jpg")
