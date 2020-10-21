# test trying to open an image without being given a path
# expect to get
# TypeError: read_img() missing 1 required positional argument: 'imgpath'

from drkrm.src import drkrm
import pytest


def test_path_empty():
    with pytest.raises(TypeError) as e:
        drkrm.read_img()
    print(e)
