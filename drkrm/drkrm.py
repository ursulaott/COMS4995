from PIL import Image
from PIL import ImageFilter


def get_path():
    path = "../examples/kakashi.jpg"
    return path


def get_input_path():
    upath = input("enter image path: ")
    return upath


def read_img(imgpath):
    im = Image.open(imgpath)
    return im


def square(im):  # returns square central crop of image
    w, h = im.size
    print(w, h)
    if w == h:
        return im
    elif w > h:  # horiz im
        buffer = w / 4
        area = (buffer, 0, h + buffer, h)
        square = im.crop(area)
    else:  # horiz im
        buffer = h / 4
        area = (0, buffer, w, w + buffer)
        square = im.crop(area)
    return square


def blur(im):
    out = im.filter(ImageFilter.BLUR)
    return out
