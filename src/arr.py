from PIL import Image
import numpy as np
import random


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


def noise(arr, amount):  # amount suggested from 10 to 50
    for row in arr:
        for pixel in row:
            pixel[0] = pixel[0] + random.gauss(0, amount)
            pixel[1] = pixel[1] + random.gauss(0, amount)
            pixel[2] = pixel[2] + random.gauss(0, amount)
    return arr
