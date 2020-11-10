# test trying to open an image without being given a path
# expect to get
# TypeError: read_img() missing 1 required positional argument: 'imgpath'

from base import *
import pytest
import sys
sys.path.insert(0, 'src')


def test_path_empty():
    with pytest.raises(TypeError) as e:
        read_img()
    print(e)
