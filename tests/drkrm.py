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
    #im.show()

# returns square central crop of image
def square(im):
    w, h = im.size
    print(w,h)
    if w == h:
        return im
    elif w > h: # horiz im
        l = w/4
        area = (l, 0, h + l, h)
        square = im.crop(area)
    else: # horiz im
        l = h/4
        area = (0, l, w, w+l)
        square = im.crop(area)
    return square


# to appease flake8

if __name__ == "__main__":
    p = get_path()
    i = read_img(p)
    sq = square(i)
    sq.show()

    i2 = read_img("../examples/bnha.jpg")
    sq2 = square(i2)
    sq2.show()
