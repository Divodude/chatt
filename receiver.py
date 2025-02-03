import serial
import struct
import io
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
baudrate =460800
ser = serial.Serial("COM4", baudrate, timeout=1)
received_chunks = {}

def save_image(received_chunks):
    sorted_chunks = [received_chunks[i] for i in sorted(received_chunks.keys())]
    image_data = b"".join(sorted_chunks).rstrip(b'\x00')

    buffer = io.BytesIO(image_data)
    try:
        img = Image.open(buffer)
        img_np = np.array(img)
        
        img_np=cv2.resize(img_np,(500,400))
        
        image_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB) 
        cv2.imshow("Received Frame", image_rgb)
        cv2.waitKey(1)  # Show frame temporarily
        img.save("received_image.png") 
        #print("Image reconstructed successfully.")
    except Exception as e:
        print(f"Error: {e}")

while True:
    header = ser.read(2)
    if header == b'ST':  # Start signal
        total_chunks = struct.unpack("H", ser.read(2))[0]
        received_chunks.clear()
        #print(f"Receiving {total_chunks} chunks...")

        for _ in range(total_chunks):
            chunk = ser.read(32)
            if chunk:
                chunk_index = struct.unpack("H", chunk[:2])[0]
                chunk_data = chunk[2:]
                received_chunks[chunk_index] = chunk_data
                save_image(received_chunks)
    elif header == b'EN':  # End signal
        print("Transmission complete.")
        break

cv2.destroyAllWindows()
