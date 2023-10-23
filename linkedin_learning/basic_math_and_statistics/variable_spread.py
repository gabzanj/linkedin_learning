import pandas as pd

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars_num = df_cars.drop('name', axis=1)

standart_variation = df_cars_num.std()
variance = df_cars_num.var()

value_counts = df_cars_num['mpg'].value_counts()

statistical_description = df_cars_num.describe()
