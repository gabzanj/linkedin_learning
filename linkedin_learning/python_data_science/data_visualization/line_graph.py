import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns

# se estiver no jupyter, use na primeira linha para mostrar os gráficos nos quadros:
# %matplotlib inline
# definir tamanho das imagens em polegadas (altura, largura)
rcParams['figure.figsize'] = 5, 4
# estilo do gráfico (whitegrid = fundo branco com grade cinza)
sns.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]

# plotar/imprimir/graficar x e y
# plt.plot(x, y)
# plt.show()

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars_filtered = df_cars[['cyl', 'mpg', 'wt']]

plt.plot(df_cars_filtered)
plt.show()
# df_cars_filtered.plot()
