# Learnumpy

A friendly Python playground for learning NumPy with clear examples, hands-on demos, and reusable code snippets.

## Repo structure

- `1.conversion from other python structures/`
  - `1.py` — create a 1D NumPy array with a specified integer dtype
  - `2.py` — create a 2D single-row NumPy array and access elements
  - `3.py` — convert a nested Python list into a 2D NumPy array
  - `4.py` — convert a Python set into a NumPy array

- `2.intrinsic numpy array creation objects/`
  - `1.py` — create arrays of zeros with `np.zeros`
  - `2.py` — generate a range of values with `np.arange`
  - `3.py` — create evenly spaced values with `np.linspace`
  - `4.py` — allocate an uninitialized array with `np.empty`
  - `5.py` — create an array with the same shape as another using `np.empty_like`
  - `6.py` — build an identity matrix with `np.identity`
  - `7.py` — reshape a 1D array into a 2D array with `reshape`

- `3.numpy axis/`
  - `1.py` — sum values along axis 0 and axis 1
  - `2.py` — transpose a 2D array with `arr.T`
  - `3.py` — iterate over array elements with `arr.flat`
  - `4.py` — show array metadata: `ndim`, `size`, `nbytes`
  - `5.py` — use `argmax`, `argmin`, and `argsort` on a 1D array
  - `6.py` — use axis-aware `argmax`, `argmin`, and `argsort` on a 2D array
  - `7.py` — add and multiply two 2D arrays element-wise
  - `8.py` — find positions with `np.where`
  - `9.py` — count nonzero values and find nonzero positions
  - `10.py` — compare Python list memory usage with NumPy array memory usage

- `tempCodeRunnerFile.py` — scratch/demo file printing array dtype and shape.

## Getting started

1. Activate the virtual environment:
   - `.\.venv\Scripts\Activate.ps1`

2. Run an example file:
   - `python "1.conversion from other python structures\1.py"`
   - `python "2.intrinsic numpy array creation objects\3.py"`
   - `python "3.numpy axis\7.py"`

3. Modify the code and rerun it to explore NumPy behavior.

## Learn by doing

- Change array values and shapes to see how operations behave
- Try broadcasting, indexing, slicing, and arithmetic across arrays
- Add your own example files for new NumPy functions

Happy learning! 🚀
