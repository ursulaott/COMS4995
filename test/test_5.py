# test trying to open a path that does not contain an image
# expect to get
# No such file or directory: '../examples/nonexistient.jpg'
# filenotfounderror is not defined in python2?

from base import *
import pytest
import sys
sys.path.insert(0, 'src')


def test_path_empty():
    with pytest.raises(IOError):
        read_img("../examples/nonexistient.jpg")
