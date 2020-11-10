# test centrally square cropping a horizontal image
import sys
sys.path.insert(0, 'src')
from src.base import *
from src.utils import *
import pytest


def test_square_horizontal():
    i2 = read_img("examples/kakashi.jpg")
    sq2 = square(i2)
    sq2.show()
