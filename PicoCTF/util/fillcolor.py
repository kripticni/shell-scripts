from PIL import Image


def fillcolor(path, target, new):
    img = Image.open(path)
    img = img.convert("RGB")

    pixels = img.getdata()
    new_pixels = list()

    for pixel in pixels:
        if pixel == target:
            new_pixels.append(new)
        else:
            new_pixels.append(pixel)

    img.putdata(new_pixels)
    img.save("filled.png")
    print("Image saved as 'filled.png'.")


# pixel values are to be inputed as tuples
