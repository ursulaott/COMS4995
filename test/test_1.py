import pytest
import sys
sys.path.insert(0, 'src')
import pathlib
print("path: ",pathlib.Path().absolute())
from src.base import *


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
