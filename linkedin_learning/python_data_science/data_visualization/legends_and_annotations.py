import pandas as pd
from matplotlib import rcParams
from matplotlib import pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches

rcParams['figure.figsize'] = 12, 6
sns.set_style('whitegrid')

x = range(1, 10)
y = [1, 2, 3, 4, .5, 4, 3, 2, 1]
# plt.bar(x, y)
# plt.xlabel('X axis title')
# plt.ylabel('Y axis title')

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
mpg = df_cars['mpg']
plt.plot(mpg)

plt.xlabel('Car name')
plt.ylabel('Miles/Gallon')
plt.title('Gasoline consumption')
plt.xticks(mpg.index, df_cars['name'], rotation=45)
# legendas
legend = mpatches.Patch(label='mpg')
plt.legend(handles=[legend])

# ponto mais alto
peak_data = mpg.max()
# anotação/texto; arrowprops são informações sobre seta
plt.annotate('Toyota Corolla', xy=(19, peak_data), xytext=(21, 33),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.show()
