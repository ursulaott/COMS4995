# test adding noise to image

import pytest
import sys
sys.path.insert(0, 'src')
from utils import *
from base import *
from arr import *


def test_sort_rows():
    i2 = read_img("examples/beach.jpg")
    npa = get_nparray_from_img(i2)
    a = sort_rows(npa, 7)
    b = get_img_from_nparray(a)
    b.show()

test_sort_rows()
