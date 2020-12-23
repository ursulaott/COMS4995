from PIL import Image
import numpy as np
import random


def get_nparray_from_img(im):
    out = np.array(im)
    return out


def get_img_from_nparray(arr):
    out = Image.fromarray(arr)
    return out


def reds(arr, percent):  # dial all reds based on percent
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


def greens(arr, percent):  # dial all greens based on percent
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


def blues(arr, percent):  # dial all blues based on percent
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


def shadows(arr):
    for row in arr:
        for pixel in row:  # remember pixels are (red, green, blue)
            p = 0
            p += pixel[0]
            p += pixel[1]
            p += pixel[2]
            if (p < 110):  # this is the threshold for detecting a "shadow"
                # do something to the shadows here!!
                pixel[0] = pixel[0]/1.2
                pixel[1] = pixel[1]/1.2
                pixel[2] = pixel[2]*1.2
                # this setting makes them bluer

    return arr


def highlights(arr):
    for row in arr:
        for pixel in row:  # remember pixels are (red, green, blue)
            p = 0
            p += pixel[0]
            p += pixel[1]
            p += pixel[2]
            if (p < 600):  # this is the threshold for detecting a "highlight"
                # do something to the highlight here!!
                pixel[0] = pixel[0]*1.2
                pixel[1] = pixel[1]
                pixel[2] = pixel[2] * 1.3
                # this setup makes highlights more orange
    return arr


def noise(arr, amount):  # amount suggested from 10 to 50
    for row in arr:
        for pixel in row:
            pixel[0] = pixel[0] + random.gauss(0, amount)
            pixel[1] = pixel[1] + random.gauss(0, amount)
            pixel[2] = pixel[2] + random.gauss(0, amount)
    return arr


def sort_rows(arr, n): # pixel sorting filter by amount n
    sorted = []
    for row in arr:
        for i in range(len(row) - n):
            p1 = row[i][0] + row[i][1] + row[i][2]
            p2 = row[i+n][0] + row[i+n][1] + row[i+n][2]
            if p1 > p2:
                y = row[i]
                row[i] = row[i+n]
                row[i+n] = y
    return arr


def partial_sort_rows(arr, n): # pixel sorting filter by amount n
    sorted = []
    for row in arr:
        for i in range(len(row) - n):
            r = random.gauss(0, 1)
            p1 = row[i][0] + row[i][1] + row[i][2]
            p2 = row[i+n][0] + row[i+n][1] + row[i+n][2]
            if p1 > p2 and (r > 0.5):
                y = row[i]
                row[i] = row[i+n]
                row[i+n] = y
    return arr


def bake(arr):  # unifinished! do not use
    for row in arr:
        for pixel in row:
            print(pixel)


def sortHelper(a):
    return a[0] + a[1] + a[2]

def interval_sort_grid(arr): # unfinished! do not use
    sorted = []
    for i in range(len(arr) - 3):
            li = []
            for x in range(0,10):
                li.append(arr[i+x])
            li = li.sort(key=sortHelper)
            for y in range(0,10):
                arr[i+y] = li[y]
    return arr
