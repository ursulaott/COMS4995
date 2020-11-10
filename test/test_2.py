# test reading in an image
# should return no errors
import sys
sys.path.insert(0, '../src')
from src.base import *
import pytest

p = get_path()

def test_path():
    assert (p != None)
