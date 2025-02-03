#Basic Code
from PIL import Image
import io

def image_to_byte_array(image_path):
    with Image.open(image_path) as img:
        img_byte_array = io.BytesIO()
        img.save(img_byte_array, format=img.format)
        return img_byte_array.getvalue()

def receive(buffer, chunk):
    buffer.write(chunk)

def buffer_to_image(buffer):
    buffer.seek(0)
    img = Image.open(buffer)
    img.show()
    return "done"

buffer = io.BytesIO()

binary_data = image_to_byte_array("Screenshot 2024-11-26 233808.png")

chunk_size = 32



for i in range(0, len(binary_data), chunk_size):
    chunk = binary_data[i:i + chunk_size] 
    receive(buffer, chunk) 

buffer_to_image(buffer)
