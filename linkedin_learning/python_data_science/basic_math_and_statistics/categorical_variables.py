import pandas as pd

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars.index = df_cars['name']

cat_cars = df_cars[['cyl', 'am', 'gear', 'carb']]
gear_groups = cat_cars.groupby('gear')
descriptive_statistics = gear_groups.describe().T

df_cars['group'] = pd.Series(df_cars['gear'], dtype='category')

cross_tab = pd.crosstab(df_cars['am'], df_cars['gear'])
