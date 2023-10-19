import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.arange(36).reshape(6, 6))
df2 = pd.DataFrame(np.arange(15).reshape(5, 3))

# considera índices das colunas axis=0
df_concatenated_columns = pd.concat([df1, df2])
# considera índices das linhas axis=1
df_concatenated_rows = pd.concat([df1, df2], axis=1)
