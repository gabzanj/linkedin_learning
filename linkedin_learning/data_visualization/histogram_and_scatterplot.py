import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
import seaborn as sns

rcParams['figure.figsize'] = 6, 4
sns.set_style('whitegrid')

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
mpg = df_cars['mpg']

plt.hist(mpg)
sns.displot(mpg)
plt.show()

# Scatter Plot
df_cars.plot(kind='scatter', x='hp', y='mpg', c=['darkgray'], s=150)
sns.regplot(x='hp', y='mpg', data=df_cars, scatter=True)

# pairplot cria uma matriz de gráficos de dispersão em pares de variáveis do df
sns.pairplot(df_cars)

columns = ['mpg', 'disp', 'hp', 'wt']
new_df = pd.DataFrame(df_cars[columns].values, columns=columns)
cars_target = df_cars['am'].values

new_df['group'] = pd.Series(cars_target, dtype='category')
# hue colore os pontos no gráfico, palette define a paleta de cores
sns.pairplot(new_df, hue='group', palette='hls')

# Boxplot
df_cars.boxplot(column='mpg', by='am')
df_cars.boxplot(column='wt', by='am')
sns.boxplot(x='am', y='mpg', data=df_cars, palette='hls')
plt.show()
