from PIL import Image


def get_path():
    path = "../examples/kakashi.jpg"
    return path


def get_input_path():
    upath = input("enter image path: ")
    return upath


def read_img(imgpath):
    im = Image.open(imgpath)
    return im
