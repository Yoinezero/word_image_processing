from PIL import Image


def get_color(image: str) -> tuple[int, int, int]:
    im = Image.open(image, 'r')
    pixels = list(im.getdata())

    count, red, green, blue = 1, 0, 0, 0
    for pixel in pixels:
        count += 1
        if type(pixel) != tuple:
            red += pixel
            green += pixel
            blue += pixel
        else:
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]

    im.close()
    return red // count, green // count, blue // count
