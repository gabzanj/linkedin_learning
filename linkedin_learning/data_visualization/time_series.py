import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import rcParams
import seaborn as sns

rcParams['figure.figsize'] = 5, 4
sns.set_style('whitegrid')

arq_path = f'../files/Superstore-Sales.csv'
df_sales = pd.read_csv(arq_path, index_col='Order Date', parse_dates=True, encoding='ISO-8859-1')

# df_sales['Order Quantity'].plot()
# plt.show()

# melhorar visualização diminuindo a quantidade de observações (ex: 100)
df2_sales = df_sales.sample(n=100, random_state=25, axis=0)
plt.xlabel('Order Date')
plt.ylabel('Order Quantity')
plt.title('Sales')
df2_sales['Order Quantity'].plot()

plt.show()