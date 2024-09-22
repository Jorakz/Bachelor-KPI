import pandas as pd
import numpy as np
from math import comb
def task(cluster_data, k):
    cluster_mean = [cluster_data[i].mean(axis=0) for i in range(len(cluster_data))]
    cluster_dev = [0] * len(cluster_data)
    ans = [0, 0]
    print("Розбиття на ",k, "кластерів\n")
    l = 1
    x = 0
    for q in range(1,3):
      for i, cluster in enumerate(cluster_data):
        for j in cluster:
            x += np.sum((j - cluster_mean[i]) **2) ** (1/q)
        cluster_dev[i] = x / len(cluster)
        x = 0
      cluster_dev_mean = np.sum(cluster_dev)/len(cluster_data)

      sum = 0
      for i in range(len(cluster_data)):
          for j in range(i + 1, len(cluster_data)):
            sum = np.sum((cluster_mean[i] - cluster_mean[j])**2 )**(1/q) + sum
      clusters = sum / comb(len(cluster_data),2)

      ans[q-1] = np.array([cluster_dev_mean,clusters,cluster_dev_mean/clusters])

      if l == 1:
          print("Чисельник - ", cluster_dev_mean, '\nЗнаменник - ', clusters,'\nКритерій роздільності через середньоквадратичне відхилення  - ', cluster_dev_mean / clusters,"\n")
          l = l - 1
      else:
         print("Чисельник - ",cluster_dev_mean,'\nЗнаменник - ',clusters,'\nКритерій роздільності через евклідової норми - ',cluster_dev_mean/clusters,"\n")
         l = l + 1

    print("\n")

    return ans

df = pd.read_excel('lab_1.xlsx', engine='openpyxl')


df_8 = [df[df["Cl8_APHR"] == i + 1].drop(columns=['Cl8_APHR', 'Cl12_APHR', 'Cl14_APHR']).values for i in range(8)]
df_12 = [df[df["Cl12_APHR"] == i + 1].drop(columns=['Cl8_APHR', 'Cl12_APHR', 'Cl14_APHR']).values for i in range(12)]
df_14 = [df[df["Cl14_APHR"] == i + 1].drop(columns=['Cl8_APHR', 'Cl12_APHR', 'Cl14_APHR']).values for i in range(14)]

result_1 = [0,0,0]
result_2 = [0,0,0]
var = ['Cl8_APHR', 'Cl12_APHR', 'Cl14_APHR']
result_1[0],result_2[0] =task(df_8, 8)

result_1[1],result_2[1] =task(df_12, 12)

result_1[2],result_2[2] =task(df_14, 14)

print("Мінімальне значення чисельника для середньоквадратичного відхилення: ",var[np.argmin(np.array(result_2), axis=0)[0]])
print("Максимальне значення знаменника для середньоквадратичного відхилення: ",var[np.argmax(np.array(result_2), axis=0)[1]])
print("Мінімальна значення відношення для середньоквадратичного відхилення: ",var[np.argmin(np.array(result_2), axis=0)[2]])
print("Мінімальна значення чисельника для Евклідової норми: ",var[np.argmin(np.array(result_1), axis=0)[0]])
print("Максимальне значення знаменника для Евклідової норми: ",var[np.argmax(np.array(result_1), axis=0)[1]])
print("Мінімальна значення відношення для Евклідової норми: ",var[np.argmin(np.array(result_1), axis=0)[2]])


