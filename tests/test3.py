# test reading opening an image
# should return by opening an image of kakashi sensei
import drkrm
import pytest

p = drkrm.get_path()

def test_open_img():
    assert (p != None)

drkrm.read_img(p)
