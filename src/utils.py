from PIL import ImageFilter


def square(im):  # returns square central crop of image
    w, h = im.size
    print(w, h)
    if w == h:
        return im
    elif w > h:  # horiz im
        buffer = w / 4
        area = (buffer, 0, h + buffer, h)
        square = im.crop(area)
    else:  # vert im
        buffer = h / 4
        area = (0, buffer, w, w + buffer)
        square = im.crop(area)
    return square


def blur(im):  # gaussian blur
    out = im.filter(ImageFilter.BLUR)
    return out


def hex_to_rgb(hex_color):
    if hex_color[0] == '#':  # trim pound sign
        hex_color = hex_color[1:]
    out = []
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    out.append(red)
    out.append(green)
    out.append(blue)
    return out
