# API

## Base Image functions

```eval_rst
.. automodule:: src.base
   :members:
   :undoc-members:
   :show-inheritance:
```

```eval_rst
.. automodule:: src.base.get_path
   :members:
   :undoc-members:
   :show-inheritance:
```
get sample/example image path

```eval_rst
.. automodule:: src.base.get_input_path
   :members:
   :undoc-members:
   :show-inheritance:
```
get image path from user input

```eval_rst
.. automodule:: src.base.read_img
   :members:
   :undoc-members:
   :show-inheritance:
```
get image from supplied image path

## Utility functions

```eval_rst
.. automodule:: src.utils
   :members:
   :undoc-members:
   :show-inheritance:
```

```eval_rst
.. automodule:: src.utils.square
   :members:
   :undoc-members:
   :show-inheritance:
```
square crop image

```eval_rst
.. automodule:: src.utils.blur
   :members:
   :undoc-members:
   :show-inheritance:
```
blur image

```eval_rst
.. automodule:: src.utils.hex_to_rgb
   :members:
   :undoc-members:
   :show-inheritance:
```
convert hex color code to rgb

## Array functions

```eval_rst
.. automodule:: src.arr
   :members:
   :undoc-members:
   :show-inheritance:
```


```eval_rst
.. automodule:: src.arr.get_nparray_from_img
   :members:
   :undoc-members:
   :show-inheritance:
```
get numpy array from image

```eval_rst
.. automodule:: src.arr.get_img_from_nparray
   :members:
   :undoc-members:
   :show-inheritance:
```
get image from numpy array

```eval_rst
.. automodule:: src.arr.reds
   :members:
   :undoc-members:
   :show-inheritance:
```
adjust reds in image by percentage (percent less than 100 = turn down intensity, percent above 100 = turn up intensity)

```eval_rst
.. automodule:: src.arr.greens
   :members:
   :undoc-members:
   :show-inheritance:
```
adjust greens in image by percentage (percent less than 100 = turn down intensity, percent above 100 = turn up intensity)

```eval_rst
.. automodule:: src.arr.blues
   :members:
   :undoc-members:
   :show-inheritance:
```
adjust blues in image by percentage (percent less than 100 = turn down intensity, percent above 100 = turn up intensity)

```eval_rst
.. automodule:: src.arr.shadows
   :members:
   :undoc-members:
   :show-inheritance:
```
adjust shadows in image

```eval_rst
.. automodule:: src.arr.highlights
   :members:
   :undoc-members:
   :show-inheritance:
```
adjust highlights in image

```eval_rst
.. automodule:: src.arr.noise
   :members:
   :undoc-members:
   :show-inheritance:
```
add noise (suggested amount value 10 to 50)

## Math functions

## Other functions
