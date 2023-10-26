import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)
array_a = np.array([1, 2, 3, 4, 5, 6])

np.random.seed(25)
array_b = randn(6)

array_c = np.arange(1, 35)

sum_arr = array_a + array_b
subtraction_arr = array_a - array_b
multiply_arr = array_a * array_b
div_arr = array_a / array_b
