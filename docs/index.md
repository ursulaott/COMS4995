# drkrm

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/ursulaott/COMS4995/blob/master/LICENSE) ![CI](https://github.com/ursulaott/drkrm/workflows/CI/badge.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/ursulaott/drkrm)
[![codecov](https://codecov.io/gh/ursulaott/drkrm/branch/master/graph/badge.svg?token=AKEGV74WVZ)](undefined)
[![Documentation Status](https://readthedocs.org/projects/drkrm/badge/?version=latest)](https://drkrm.readthedocs.io/en/latest/?badge=latest)

drkrm | pixel-perfect photo filters in python [link to repo](https://github.com/ursulaott/COMS4995)

## installation

pip install drkrm==0.1.0

## documentation

check out documentation at [readthedocs](https://drkrm.readthedocs.io/en/latest/)

## description:
- a library of photo editing/filter effects in python that are free, easy to use, and highly fine-tune-able (kind of like lightroom presets)
- starting as a cli tool

## examples
<img src="examples/mangarecolor.png" alt="manga recolor" height="400" /> <img src="examples/beach.jpg" alt="normal photo editing" height="400" />
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
