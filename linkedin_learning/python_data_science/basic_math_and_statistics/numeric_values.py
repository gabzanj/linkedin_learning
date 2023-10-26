import pandas as pd

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars_num = df_cars.drop('name', axis=1)

sum_cars = df_cars.sum()
sum_rows_cars = df_cars_num.sum(axis=1)

median = df_cars_num.median()

arithmetic_average = df_cars_num.mean()

max_value = df_cars.max()
row_idxmax = df_cars_num['mpg'].idxmax()
