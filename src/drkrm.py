from PIL import Image

def get_path():
    path = "../examples/kakashi.jpg"
    return path

def read_img(imgpath):
    im = Image.open(imgpath)
    im.show()
