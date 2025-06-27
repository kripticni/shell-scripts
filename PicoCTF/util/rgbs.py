from PIL import Image


def getrgbs(path):
    img = Image.open(path)
    img = img.convert("RGB")

    pixels = list(img.getdata())
    seen_pixels = set()

    for pixel in pixels:
        if pixel not in seen_pixels:
            print(pixel)
            seen_pixels.add(pixel)
