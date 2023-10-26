import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from sklearn import preprocessing

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars.index = df_cars['name']
mpg = df_cars['mpg']

rcParams['figure.figsize'] = 6, 3
sns.set_style('whitegrid')

description = df_cars[['mpg']].describe()
# plt.plot(mpg)

# (-1, 1): -1: todas as linhas do objeto; 1: 1 coluna
mpg_matrix = mpg.values.reshape(-1, 1)
scaler = preprocessing.MinMaxScaler()
scaled_mpg = scaler.fit_transform(mpg_matrix)

# plt.plot(scaled_mpg)
# plt.show()

scaler = preprocessing.MinMaxScaler(feature_range=(0, 10))
scaled_mpg = scaler.fit_transform(mpg_matrix)
# plt.plot(scaled_mpg)
# plt.show()

mpg_standardized = preprocessing.scale(mpg, axis=0, with_mean=False, with_std=False)
# plt.plot(mpg_standardized)
# plt.show()

mpg_standardized = preprocessing.scale(mpg)
