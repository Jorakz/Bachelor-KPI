
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split


dataset = pd.read_excel('Algerian_forest_fires_dataset.xlsx')
print(dataset)
print(dataset.info())


dataset = dataset.dropna()


#dataset = dataset.replace(['fire   ','fire ','fire','not fire   ','not fire     ','not fire ','not fire    ','not fire'],[1,1,1,0,0,0,0,0])

print(dataset.info())
X = dataset.iloc[:, 3:13].to_numpy()
Y = dataset.iloc[:, 13].to_numpy()


print(dataset.info())
print(dataset)
for i in range(len(Y)):
 if 'not fire' in Y[i]:
  Y[i] = 0
 elif 'fire' in Y[i]:
  Y[i] = 1
Y = Y.astype('int64')
x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.5, shuffle=True, random_state=1)


mean = x_train.mean(axis=0)
std = x_train.std(axis=0)
x_train -= mean
x_train /= std
x_test -= mean
x_test /= std

model = keras.Sequential([
 layers.Dense(16, activation='relu', input_shape=(x_train.shape[1],)),
 layers.Dense(64, activation='relu'),
 layers.Dense(1)
])


model.compile(optimizer='adam',
 loss='mean_squared_error',
 metrics=['mae'])
model.summary()

print("x_train dtype:", x_train.dtype)
print("y_train dtype:", y_train.dtype)
print("x_train sample:", x_train[0])
print("y_train sample:", y_train[0])

history = model.fit(x_train, y_train, validation_split=0.2, epochs=1000)

# Навчання моделі і зберігання історії

test_loss, test_mae = model.evaluate(x_test, y_test)
print(f"Test Loss: {test_loss}")
print(f"Mean Absolute Error on Test Data: {test_mae}")

predictions = model.predict(x_test)

print('результати з бази даних:\n',y_test[:5])
print('результати прогнозу:\n',predictions[:5])


# Побудова графіка втрат
plt.figure(figsize=(12,4))
plt.subplot(1,2,1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss Value')
plt.legend()
# Побудова графіка метрики (наприклад, MAE)
plt.subplot(1,2,2)
plt.plot(history.history['mae'], label='Training MAE')
plt.plot(history.history['val_mae'], label='Validation MAE')
plt.title('Training and Validation MAE')
plt.xlabel('Epoch')
plt.ylabel('MAE Value')
plt.legend()
plt.tight_layout()
plt.show()
