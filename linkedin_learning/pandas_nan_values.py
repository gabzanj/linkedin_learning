import numpy as np
from pandas import Series, DataFrame

blank_value = np.nan

serie_with_nan_values = Series(['row 1', 'row 2', blank_value, 'row 4', 'row 5', blank_value, 'row 8'])
print(serie_with_nan_values.isnull())
