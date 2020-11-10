# test centrally square cropping a vertical image

import pytest
from src.utils import *
from src.base import *
import sys
sys.path.insert(0, '../src')


def test_square_vertical():
    i2 = read_img("examples/bnha.jpg")
    sq2 = square(i2)
    sq2.show()
