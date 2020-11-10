# test getting a supplied image path

from base import *
import pytest
import sys
sys.path.insert(0, 'src')


p = "examples/kakashi.jpg"


def test_open_img():
    assert (p != None)

# figure out how to simulate user input in test?
