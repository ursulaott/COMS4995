from PIL import Image

def get_path():
    path = "kakashi.jpg"
    return path

def input_path():
    upath = input("enter image path: ")
    return upath

def read_img(imgpath):
    im = Image.open(imgpath)
    im.show()
