import numpy as np
from numpy.random import randn

np.set_printoptions(precision=2)

array_a = np.arange(3)
matrix_a = np.array([[2., 4., 5.], [1., 4., 8.], [12., 13., 15.]])
multiplication = array_a * matrix_a

matrix_b = np.arange(9).reshape((3, 3))
mult_matrix = np.dot(matrix_a, matrix_b)

array_b = array_a * 3
dot_product = np.dot(array_a, array_b)
