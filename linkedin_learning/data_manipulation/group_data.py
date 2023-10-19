import pandas as pd

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)

# ignorar erros na coluna não numerica
df_cars['name'] = pd.to_numeric(df_cars['name'], errors='coerce')
grouping_col = df_cars['cyl']
grouped_cars = df_cars.groupby(grouping_col)
means = grouped_cars.mean()

# remover colunas não numéricas e calcular média total
df_numeric = df_cars.select_dtypes(include=[float, int])
columns_means = df_numeric.mean()
