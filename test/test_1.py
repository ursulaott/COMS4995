import pytest
from src.base import *
import sys
sys.path.insert(0, '../src')


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
