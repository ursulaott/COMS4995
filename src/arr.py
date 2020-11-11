from PIL import Image
import numpy as np


def get_nparray_from_img(im):
    out = np.array(im)
    return out


def get_img_from_nparray(arr):
    out = Image.fromarray(arr)
    return out


def reds(arr, percent):  # dial reds based on percent
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


def greens(arr, percent):  # dial greens based on percent
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


def blues(arr, percent):  # dial blues based on percent
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
