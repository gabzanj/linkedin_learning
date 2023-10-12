import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# retornar array unidimensional de x itens
data = np.arange(8)
# reorganizar em x linhas e y colunas
data_reshaped = data.reshape((4, 2))

index = ['row 1', 'row 2', 'row 3', 'row 4',
         'row 5', 'row 6', 'row 7', 'row 8']
# Series é uma linha ou coluna indexada
series_obj = Series(data, index=index)
read_index = series_obj['row 7']

# semear randomicos
np.random.seed(25)

# criar DataFrame 6x6 com 36 valores aleatórios
index = ['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6']
columns = ['col 1', 'col 2', 'col 3', 'col 4', 'col 5', 'col 6']
df = DataFrame(np.random.rand(36).reshape((6, 6)),
               index=index, columns=columns)

df_filtered = df.loc[['row 3', 'row 6'], ['col 1', 'col 5']]
series_filtered = series_obj['row 3': 'row 7']

df_test = df < .2

filter_data = series_obj > 6
series_greater_x = series_obj[filter_data]

# atualizar valores
series_obj.loc[['row 1', 'row 3', 'row 5']] = 8
