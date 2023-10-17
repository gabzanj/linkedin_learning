import numpy as np
from pandas import Series, DataFrame

blank_value = np.nan

serie_with_nan_values = Series(['row 1', 'row 2', blank_value, 'row 4', 'row 5', blank_value, 'row 8'])
null_values = serie_with_nan_values.isnull()

np.random.seed(25)
df = DataFrame(np.random.rand(36).reshape(6, 6))
# linha A a B na coluna C [A:B, C]
df.loc[3:5, 0] = blank_value
df.loc[1:4, 5] = blank_value

df_filled = df.fillna(0)
dict_replace = {0: 0.1, 5: 1.25}
df_dict_filled = df.fillna(dict_replace)

sum_null_values = df.isnull().sum()
df_row_without_nan = df.dropna()
df_col_without_nan = df.dropna(axis=1)
