import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.DataFrame({
# 	'unif' : np.random.uniform(-3, 3, 20)
# 	,'norm' : np.random.normal(0, 1, 20)
# })

df = pd.DataFrame(np.random.randn(10, 4), columns=['Col1', 'Col2', 'Col3', 'Col4'])
#print(df.head())
boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3'])
#plt.show()
#	Show 하는 방법 연구 요망

np.random.seed(1234)
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['Col1', 'Col2', 'Col3', 'Col4'])
boxplot = df.boxplot(column=['Col1', 'Col2', 'Col3'])  
plt.show()

#df.index = pd.date_range('2000', freq='Y', periods=df.shape[0])
#plt.plot(df.plot())
#plt.show()

# df.index = pd.date_range('2000', freq='Y', periods=df.shape[0])
# df.plot()