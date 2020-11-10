# test getting a supplied image path

import sys
sys.path.insert(0, '../src')
from src.base import *
import pytest

p = "examples/kakashi.jpg"


def test_open_img():
    assert (p != None)

# figure out how to simulate user input in test?
