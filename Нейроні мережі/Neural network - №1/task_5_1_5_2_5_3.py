import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.datasets import load_digits
datas = load_digits()
df = pd.DataFrame(datas.data)

print(df.mean() , ' - Pandas\n')
print(df[1].value_counts())
datas_mean = np.array(df.mean)
d = np.array(datas.data)
d_mean = np.mean(d,axis=0)
d_mean_correct =(np.array([np.format_float_positional(x, precision=6) for x in d_mean ]))
print(d_mean_correct, ' - NumPy')

fig, axes = plot.subplots(nrows=8, ncols=8, figsize=(16, 16))
#print(datas.data)
#print(df)

for i in range(8):

    for j in range(8):
        ax = axes[i, j]
        attribute = datas.data[:, i * 8 + j]
        #ax.hist(attribute, bins=20, alpha=0.35)
        ax.boxplot(attribute)
        ax.set_title(f'Атрибути {i * 8 + j}')
        ax.set_xlabel('Значення')
        ax.set_ylabel('Частота')

plot.tight_layout()
plot.show()
