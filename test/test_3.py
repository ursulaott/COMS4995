# test getting a supplied image path

from drkrm.src import drkrm
import pytest

p = "./kakashi.jpg"

def test_open_img():
    assert (p != None)

# figure out how to simulate user input in test?
