import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import Sequential
from keras.layers import Dense, Dropout
from tensorflow.keras.initializers import HeNormal, GlorotUniform
from tensorflow.keras.regularizers import l1, l2
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, f1_score

dataset = pd.read_excel('diabetes.xlsx')
print(dataset)
print(dataset.info())
dataset = dataset.dropna()
X = dataset.iloc[:, 0:8].to_numpy()
Y = dataset.iloc[:, 8].to_numpy()

x_train, x_test, y_train, y_test = train_test_split(X,Y,train_size=0.5, shuffle=True, random_state=1)
mean = np.mean(x_train, axis=0)
std = np.std(x_train, axis=0)
normalized_data = (x_train - mean) / std

mean_ = np.mean(x_train, axis=0)
std_ = np.std(x_test, axis=0)
normalized_data_ = (x_test - mean_) / std_
print('X train')
print(f"Original Mean: {np.mean(x_train, axis=0)}")
print(f"Normalized Mean: {np.mean(normalized_data, axis=0)}")
print(f"Original Std: {np.std(x_train, axis=0)}")
print(f"Normalized Std: {np.std(normalized_data, axis=0)}")
print('')
print('X test')
print(f"Original Mean: {np.mean(x_test, axis=0)}")
print(f"Normalized Mean: {np.mean(normalized_data_, axis=0)}")
print(f"Original Std: {np.std(x_test, axis=0)}")
print(f"Normalized Std: {np.std(normalized_data_, axis=0)}")
from tensorflow.keras.layers import Dense, BatchNormalization

model = Sequential()

#model.add(Dense(64, activation='relu', kernel_regularizer=l2(0.01),input_shape=(8,))) # L2 регуляризація
model.add(Dense(64, activation='relu',input_shape=(8,)))
#model.add(Dropout(0.5)) # 50% нейронів буде "відключено" під час навчання
model.add(BatchNormalization())
#model.add(Dense(64, activation='relu',kernel_regularizer=l1(0.001))) # L1
model.add(Dense(64, activation='relu'))
#model.add(Dropout(0.3)) # 30% нейронів буде "відключено" під час навчання
model.add(BatchNormalization())
model.add(Dense(1, activation='sigmoid'))



model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])


model.summary()

history = model.fit(x_train, y_train, validation_split=0.2, epochs=100)
print("x_train dtype:", x_train.dtype)
print("y_train dtype:", y_train.dtype)
print("x_train sample:", x_train[0])
print("y_train sample:", y_train[0])

plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['mae'])
plt.plot(history.history['val_mae'])
plt.title('Model MAE')
plt.ylabel('MAE')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')

plt.tight_layout()
plt.show()
from sklearn.metrics import mean_absolute_error, mean_squared_error, accuracy_score, f1_score
y_pred = model.predict(x_test)
y_pred = (y_pred > 0.5)
y_pred_ = model.predict(x_train)
y_pred_ = (y_pred_ > 0.5)

accuracy_test = accuracy_score(y_test, y_pred)
mae_test  = mean_absolute_error(y_test, y_pred)
mse_test  = mean_squared_error(y_test, y_pred)
f1_test  = f1_score(y_test, y_pred)

accuracy_train = accuracy_score(y_train, y_pred_)
mae_train  = mean_absolute_error(y_train, y_pred_)
mse_train  = mean_squared_error(y_train, y_pred_)
f1_train  = f1_score(y_train, y_pred_)
print('')
print('На тестовій даних')
print(f"Точність = {accuracy_test }")
print(f"Mean Squared Error (MSE) = {mse_test }")
print(f"Mean Absolute Error (MAE) = {mae_test }")
print(f"F1-міра = {f1_test }")
print('')
print('На тренувальних даних')
print(f"Точність = {accuracy_train}")
print(f"Mean Squared Error (MSE) = {mse_train}")
print(f"Mean Absolute Error (MAE) = {mae_train}")
print(f"F1-міра = {f1_train}")