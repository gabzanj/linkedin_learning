import numpy as np
from pandas import Series, DataFrame


data = {
    'column 1': [1, 1, 2, 2, 3, 3, 3],
    'column 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'column 3': ['D', 'A', 'B', 'B', 'C', 'C', 'C'],
}

df = DataFrame(data)
df.duplicated()
df_specific_column = df.drop_duplicates(['column 3'])

df.drop_duplicates(inplace=True)
