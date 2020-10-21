# test reading in an image
# should return no errors
from src import drkrm
import pytest

p = drkrm.get_path()

def test_path():
    assert (p != None)
