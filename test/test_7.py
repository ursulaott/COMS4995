# test centrally square cropping a horizontal image

from utils import *
from base import *
import pytest
import sys
sys.path.insert(0, 'src')


def test_square_horizontal():
    i2 = read_img("examples/kakashi.jpg")
    sq2 = square(i2)
    sq2.show()
