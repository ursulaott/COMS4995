from PIL import Image
import numpy as np


def get_nparray_from_img(im):
    out = np.array(im)
    return out

# dial reds to a percentage (> 0 only)
def reds(arr, percent: int):
    if (percent < 0):
        return
    for row in arr:
        for pixel in row:
            red = pixel[0]
            red = red * (percent/100)
            if (red > 255):
                red = 255
            pixel[0] = red
    return arr

# dial reds to a percentage (> 0 only)
def greens(arr, percent: int):
    if (percent < 0):
        return
    for row in arr:
        for pixel in row:
            green = pixel[1]
            green = green * (percent/100)
            if (green > 255):
                green = 255
            pixel[1] = green
    return arr

# dial blues to a percentage (> 0 only)
def blues(arr, percent: int):
    if (percent < 0):
        return
    for row in arr:
        for pixel in row:
            blue = pixel[2]
            blue = blue * (percent/100)
            if (blue > 255):
                blue = 255
            pixel[2] = blue
    return arr

def get_img_from_nparray(arr):
    out = Image.fromarray(arr)
    return out
