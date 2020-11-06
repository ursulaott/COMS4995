# test trying to open a path that does not contain an image
# expect to get
# No such file or directory: '../examples/nonexistient.jpg'
# filenotfounderror is not defined in python2?

import drkrm
import pytest


def test_path_empty():
    with pytest.raises(IOError):
        drkrm.read_img("../examples/nonexistient.jpg")
