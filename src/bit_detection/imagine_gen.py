import numpy as np
from PIL import Image, ImageDraw, ImageFont

class image_generator():
    def __init__(self):
        pass

    def generate_noisy_image(self, height: int, width: int, color: bool = True, filename: str = None) -> Image.Image:
        noise = np.random.randint(0, 256, (height, width, 3) if color else (height, width), dtype=np.uint8)
        img = Image.fromarray(noise, mode='RGB' if color else 'L')
        if filename: 
            img.save(filename)
        return img
    
    def insert_into_image(self, img: Image.Image, text: str = "Hello World", filename: str = None) -> Image.Image:
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Hiragino Sans GB.ttc", 80)

        draw.text((100, 100), text, fill=(255, 255, 255), font=font)
        
        if filename:
            img.save(filename)
        return img