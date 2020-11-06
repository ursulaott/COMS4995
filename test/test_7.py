# test centrally square cropping a horizontal image

import drkrm
import pytest


def test_square_horizontal():
    i2 = drkrm.read_img("examples/kakashi.jpg")
    sq2 = drkrm.square(i2)
    sq2.show()
