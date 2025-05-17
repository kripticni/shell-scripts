from PIL import Image

img = Image.open("advanced-potion-making.png")
img = img.convert("RGB")

pixels = list(img.getdata())
freq_pixels = dict()

for pixel in pixels:
    if pixel in freq_pixels:
        freq_pixels[pixel] += 1
    else:
        freq_pixels[pixel] = 1

for pixel, frequency in freq_pixels.items():
    print(f"{pixel} : {frequency}")
