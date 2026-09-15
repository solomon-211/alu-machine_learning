# Linear Algebra

This is the first math project for the ML foundations track. It's
basically a warm-up on vectors and matrices before we get into the
heavier stuff — slicing, shapes, transposing, adding/multiplying
matrices, and then doing the same things again but with numpy so we
can see why it's so much faster than plain Python loops.

I did the first 9 tasks with just plain Python (no imports allowed),
then switched over to numpy for the rest.

## What I learned

- A vector is just a 1D array of numbers, a matrix is a 2D (or
  higher) array of numbers.
- The shape of a matrix tells you how many elements are in each
  dimension, e.g. a 2x3 matrix has 2 rows and 3 columns.
- Transposing flips rows into columns and vice versa.
- Slicing lets you grab a chunk of a list/array using start:stop
  indices, and it works the same way on nested lists if you slice
  each row individually.
- Element-wise operations happen position by position (arr1[i] +
  arr2[i]), as opposed to matrix multiplication which uses the dot
  product of rows and columns.
- Concatenation glues two arrays/matrices together along a given
  axis (axis=0 stacks rows, axis=1 stacks columns).
- Numpy does all of this way faster than plain Python because it
  runs the loops in optimized C code instead of the Python
  interpreter, and it can broadcast smaller arrays to match bigger
  ones without manually looping.

## Files

- `0-slice_me_up.py` - slicing a list into pieces
- `1-trim_me_down.py` - grabbing the middle columns of a matrix
- `2-size_me_please.py` - `matrix_shape(matrix)`
- `3-flip_me_over.py` - `matrix_transpose(matrix)`
- `4-line_up.py` - `add_arrays(arr1, arr2)`
- `5-across_the_planes.py` - `add_matrices2D(mat1, mat2)`
- `6-howdy_partner.py` - `cat_arrays(arr1, arr2)`
- `7-gettin_cozy.py` - `cat_matrices2D(mat1, mat2, axis=0)`
- `8-ridin_bareback.py` - `mat_mul(mat1, mat2)`
- `9-let_the_butcher_slice_it.py` - slicing a numpy array
- `10-ill_use_my_scale.py` - `np_shape(matrix)`
- `11-the_western_exchange.py` - `np_transpose(matrix)`
- `12-bracin_the_elements.py` - `np_elementwise(mat1, mat2)`
- `13-cats_got_your_tongue.py` - `np_cat(mat1, mat2, axis=0)`
- `14-saddle_up.py` - `np_matmul(mat1, mat2)`

## Environment

Built and tested on Ubuntu 16.04 with Python 3.5, numpy 1.15, and
pycodestyle 2.5. Every script starts with `#!/usr/bin/env python3`
and is executable.
