# test trying to open a path that does not contain an image
# expect to get
# No such file or directory: '../examples/nonexistient.jpg'

import drkrm
import pytest

def test_path_empty():
    with pytest.raises(FileNotFoundError) as e:
        drkrm.read_img("../examples/nonexistient.jpg")
        print(e)
