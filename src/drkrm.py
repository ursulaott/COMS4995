from PIL import Image

def get_path():
    path = "../examples/kakashi.jpg"
    return path

def read_img(path):
    im = Image.open(path)
    im.show()

path = get_path()
read_img(path)
