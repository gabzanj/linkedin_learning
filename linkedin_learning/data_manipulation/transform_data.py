import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(36).reshape(6, 6))

# remover dados (indicar as linhas a serem removidas)
df_row_dropped = df.drop([0, 2])
# remover dados (indicar as linhas a serem removidas)
df_column_dropped = df.drop([1, 2], axis=1)

# acrescentar dados
serie = pd.Series(np.arange(6))
serie.name = 'new_variable'
df_joined = pd.DataFrame.join(df, serie)

# ordenar dados
df_sorted = df_joined.sort_values(by=['new_variable'], ascending=True)
