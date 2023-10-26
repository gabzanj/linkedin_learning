import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
import seaborn as sns

rcParams['figure.figsize'] = 6, 4
sns.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, 5, 0, 3, 2, 1]

# plt.bar(x, y)
# plt.show()

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
mpg = df_cars['mpg']

# informar o tipo de gráfico em kind
# barras verticais: bar; barras horizontais: barh
mpg.plot(kind='bar')

# salvar gráfico como imagem
plt.savefig(f'..\\files\\bar_graph_mpg.png')
plt.show()
