import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from scipy.stats.stats import pearsonr

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars.index = df_cars['name']

rcParams['figure.figsize'] = 6, 3
sns.set_style('whitegrid')

X = df_cars[['mpg', 'hp', 'wt', 'qsec']]
# sns.pairplot(X)

mpg = df_cars['mpg']
hp = df_cars['hp']
wt = df_cars['wt']
qsec = df_cars['qsec']

pearson_coefficient, p_value = pearsonr(mpg, hp)
print('Pearson Coefficient: {:0.3}'.format(pearson_coefficient))

pearson_coefficient, p_value = pearsonr(mpg, wt)
print('Pearson Coefficient: {:0.3}'.format(pearson_coefficient))

pearson_coefficient, p_value = pearsonr(mpg, qsec)
print('Pearson Coefficient: {:0.3}'.format(pearson_coefficient))

pearson_coefficient_pandas = X.corr()
print(pearson_coefficient_pandas)

sns.heatmap(pearson_coefficient_pandas,
            xticklabels=pearson_coefficient_pandas.columns.values,
            yticklabels=pearson_coefficient_pandas.columns.values)

plt.show()
