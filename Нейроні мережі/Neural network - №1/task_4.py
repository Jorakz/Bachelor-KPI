
import pandas as pd
from sklearn.datasets import load_digits
datas = load_digits()

df = pd.DataFrame(datas.data)
#print (df[0:5])

#print(df.describe())
df['mark'] = datas.target
print(df['mark'].value_counts())