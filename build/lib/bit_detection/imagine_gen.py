import numpy as np
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

FONT = "GeistMonoNerdFontMono-Medium.otf"

FONT_PATH = str(Path(__file__).resolve().parents[2]) + f"/font/{FONT}"
class image_generator():
    def __init__(self):
        pass

    def generate_noisy_image(self, height: int, width: int, image_path: str, color: bool = True) -> None:
        noise = np.random.randint(0, 256, (height, width, 3) if color else (height, width), dtype=np.uint8)
        img = Image.fromarray(noise, mode='RGB' if color else 'L')
        img.save(image_path)

    def insert_into_image(self, image_path: str, colored: bool, message: str = "Hello World", encoding: bool = True) -> None:
        img = Image.open(image_path)
        img_x, img_y = img.size


        if not encoding:
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(str(FONT_PATH), 80)
            draw.text((img_x//2, img_y//2), message, fill=(255, 255, 255), font=font, anchor="mm")
            img.save(image_path)
            return
        
        binary_msg = ''.join(format(ord(i), '08b') for i in message) + '1111111111111110'
        pixels = list(img.getdata())
        new_pixels = []
        bit_idx = 0

        for pixel in pixels:

            if colored:
                new_pixel = list(pixel)
                for i in range(3):
                    if bit_idx < len(binary_msg):
                        # Replace LSB with the message bit
                        new_pixel[i] = (new_pixel[i] & ~1) | int(binary_msg[bit_idx])
                        bit_idx += 1
                new_pixels.append(tuple(new_pixel))
            else:
                # TODO: not complete Cant insert in black and white image
                if bit_idx < len(binary_msg):
                    new_pixel = new_pixel & ~1 | int(binary_msg[bit_idx])
                new_pixel.append(new_pixel)
        img.putdata(new_pixels)
        img.save(image_path, "PNG")
