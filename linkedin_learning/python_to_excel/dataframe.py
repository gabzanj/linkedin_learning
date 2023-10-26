import pandas as pd
import numpy as np

sequential_dates = pd.date_range('20231025', periods=6, freq='D')
matrix_row_cols = np.random.randn(6, 4)

df_dates = pd.DataFrame(matrix_row_cols, index=sequential_dates, columns=list('ABCD'))

head = df_dates.head(3)
tail = df_dates.tail(2)
shape = df_dates.shape
description = df_dates.describe()
count_elements = df_dates.count()

df_transposed = df_dates.T

df_sorted_ascending = df_dates.sort_values(by='C')
df_sorted_descending = df_dates.sort_values(by='C', ascending=False)

df_sorted_index = df_dates.sort_index(ascending=False)
df_sorted_index2 = df_dates.T.sort_index(ascending=False, axis=1)

df_range_of_values = df_dates[1:3]
df_find_row = df_dates.loc[sequential_dates[2]]

