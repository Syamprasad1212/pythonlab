import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Basic slicing: elements from index 1 to 4 (excluding 5)
slice_arr = arr[1:5]
print("Basic slicing arr[1:5]:", slice_arr)

# Integer indexing: selecting specific indices
int_index_arr = arr[[0, 2, 4]]
print("Integer indexing arr[[0, 2, 4]]:", int_index_arr)

# Boolean indexing: elements greater than 25
bool_index_arr = arr[arr > 25]
print("Boolean indexing arr[arr > 25]:", bool_index_arr)
