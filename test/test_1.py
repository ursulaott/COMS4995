import sys
sys.path.insert(0, '../src')
from src.base import *
import pytest


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
