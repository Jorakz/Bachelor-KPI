import gzip
import idx2numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense, Flatten, Reshape, Conv2D, MaxPooling2D, UpSampling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import backend as K
from tensorflow.keras.regularizers import l1, l2
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

def load_kmnist():
    with gzip.open('train-images-idx3-ubyte.gz', 'r') as f:
        x_train = idx2numpy.convert_from_file(f)
        with gzip.open('train-labels-idx1-ubyte.gz', 'r') as f:
            y_train = idx2numpy.convert_from_file(f)
            with gzip.open('t10k-images-idx3-ubyte.gz', 'r') as f:
                x_test = idx2numpy.convert_from_file(f)
            with gzip.open('t10k-labels-idx1-ubyte.gz', 'r') as f:
                y_test = idx2numpy.convert_from_file(f)
            return (x_train, y_train), (x_test, y_test)


(x_train, y_train), (x_test, y_test) = load_kmnist()

# Завантаження даних
(x_train, _), (x_test, _) = mnist.load_data()
# Нормалізація даних
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), 28, 28, 1))
x_test = x_test.reshape((len(x_test), 28, 28, 1))
#Створення моделі автоенкодера.S

# Параметри вхідних даних
input_img = Input(shape=(28, 28, 1))
# Архітектура енкодера
#x = Conv2D(8, (3, 3), activation='relu', padding='same')(input_img)
#x = Conv2D(32, (3, 3), activation='relu', padding='same')(input_img)
x = Conv2D(64, (3, 3), activation='relu', padding='same')(input_img)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
x = MaxPooling2D((2, 2), padding='same')(x)
#x = Dense(32, activation='relu')(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same')(x)
#x = Conv2D(8, (3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)
# Архітектура декодера
x = Conv2D(16, (3, 3), activation='relu', padding='same')(encoded)
#x = Conv2D(32, (3, 3), activation='relu', padding='same')(encoded)
x = UpSampling2D((2, 2))(x)
#x = Dense(32, activation='relu')(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same')(x)
#x = UpSampling2D((2, 2))(x)
#x = Conv2D(64, (3, 3), activation='relu', padding='same')(x)
#x = Conv2D(128, (3, 3), activation='relu', padding='same')(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same')(x)
# Модель автоенкодера
autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')
#Навчання автоенкодера
history = autoencoder.fit(x_train, x_train,
 epochs=10,
 batch_size=256,
 shuffle=True,
 validation_data=(x_test, x_test))
#Візуалізація результатів
decoded_imgs = autoencoder.predict(x_test)
n = 10 # скільки цифр ми відобразимо
plt.figure(figsize=(20, 4))
for i in range(n):
 # Відображення оригіналу
 ax = plt.subplot(2, n, i + 1)
 plt.imshow(x_test[i].reshape(28, 28))
 plt.gray()
 ax.get_xaxis().set_visible(False)
 ax.get_yaxis().set_visible(False)
 # Відображення відтворення
 ax = plt.subplot(2, n, i + 1 + n)
 plt.imshow(decoded_imgs[i].reshape(28, 28))
 plt.gray()
 ax.get_xaxis().set_visible(False)
 ax.get_yaxis().set_visible(False)
plt.show()
#Розрахунок метрик якості та візуалізація навчання.
# Відображення графіка функції втрат
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Model Loss')
plt.ylabel('Loss')
plt.xlabel('Epochs')
plt.legend(loc='upper right')
plt.show()
# Розрахунок та відображення MSE між оригінальними та відтвореними зображеннями
mse = np.mean(np.square(x_test - decoded_imgs), axis=(1,2,3))
print(f"Середня MSE: {np.mean(mse)}")
print(f"Стандартне відхилення MSE: {np.std(mse)}")
plt.figure(figsize=(10, 5))
plt.hist(mse, bins=50)
plt.xlabel('MSE')
plt.ylabel('Кількість зображень')
plt.show()
