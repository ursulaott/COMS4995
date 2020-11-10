# test reading in an image
# should return no errors
import pytest
from src.base import *
import sys
sys.path.insert(0, '../src')

p = get_path()


def test_path():
    assert (p != None)
