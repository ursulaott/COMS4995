# test reading in an image
# should return no errors
from drkrm.src import drkrm
import pytest

p = drkrm.get_path()

def test_path():
    assert (p != None)
