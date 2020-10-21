# test centrally square cropping a vertical image

import drkrm
import pytest

def test_square_vertical():
    i2 = drkrm.read_img("../examples/bnha.jpg")
    sq2 = drkrm.square(i2)
    sq2.show()

test_square_vertical()
