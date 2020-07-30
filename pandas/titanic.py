import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('data/titanic3.xls')
print (df.head)
df.drop(['ticket', 'cabin', 'boat', 'body'], axis=1).head()

pd.value_counts(df['survived']).plot.bar()

plt.show()