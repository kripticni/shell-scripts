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


c1 = (239, 18, 29)
c2 = (238, 17, 28)
c3 = (237, 17, 27)
replace = (0, 0, 0)

fillcolor("red.png", c1, replace)
fillcolor("filled.png", c2, replace)
fillcolor("filled.png", c3, replace)
