import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from scipy.stats.stats import spearmanr
from scipy.stats import chi2_contingency

path_csv = '../files/mtcars.csv'
df_cars = pd.read_csv(path_csv)
df_cars.rename(columns={'Unnamed: 0': 'name'}, inplace=True)
df_cars.index = df_cars['name']

rcParams['figure.figsize'] = 6, 3
sns.set_style('whitegrid')

X = df_cars[['cyl', 'vs', 'am', 'gear']]
sns.pairplot(X)
# plt.show()

cyl = df_cars['cyl']
vs = df_cars['vs']
am = df_cars['am']
gear = df_cars['gear']

coefficient, p_value = spearmanr(cyl, vs)
print('Correlation Spearman: {:0.3}'.format(coefficient))

coefficient, p_value = spearmanr(cyl, am)
print('Correlation Spearman: {:0.3}'.format(coefficient))

coefficient, p_value = spearmanr(cyl, gear)
print('Correlation Spearman: {:0.3}'.format(coefficient))

table = pd.crosstab(cyl, am)
chi2, p, dof, exp = chi2_contingency(table.values)
print('Chi-square: {:0.3}'.format(chi2, p))

table = pd.crosstab(cyl, vs)
chi2, p, dof, exp = chi2_contingency(table.values)
print('Chi-square: {:0.3}'.format(chi2, p))

table = pd.crosstab(cyl, gear)
chi2, p, dof, exp = chi2_contingency(table.values)
print('Chi-square: {:0.3}'.format(chi2, p))
