import pandas as pd
from sklearn.decomposition import FactorAnalysis
from sklearn import datasets

iris = datasets.load_iris()

X = iris.data
variable_names = iris.feature_names
print(f'5 first rows: {X[0:5, ]}')

factors = FactorAnalysis().fit(X)
df_iris = pd.DataFrame(factors.components_, columns=variable_names)
print(df_iris)
