# test centrally square cropping a horizontal image
import pytest
from src.utils import *
from src.base import *
import sys
sys.path.insert(0, '../src')


def test_square_horizontal():
    i2 = read_img("examples/kakashi.jpg")
    sq2 = square(i2)
    sq2.show()
