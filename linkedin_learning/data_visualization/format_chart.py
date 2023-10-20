import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
import seaborn as sns

rcParams['figure.figsize'] = 6, 4
sns.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, .5, 4, 3, 2, 1]

bar_color = ['salmon']
# plt.bar(x, y, color=bar_color)

x1 = range(0, 10)
# lista de numeros de 10 a 0 em ordem decrescente
y1 = list(range(10, 0, -1))

# juntar impressão dos gráficos
# ls é linestyle; lw é linewidth
plt.bar(x, y, color=bar_color, edgecolor='black', ls='-', lw=1)
# marker são os marcadores; mew é a espessura dos markers
plt.plot(x1, y1, ls='--', lw=2, marker='*', mew=10)
plt.show()



path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
mpg = df_cars['mpg']

mpg.plot(kind='bar')

