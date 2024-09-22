import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
# Завантаження даних
from tensorflow.keras.datasets import fashion_mnist
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D,  Flatten, Dense, Dropout, BatchNormalization
import matplotlib.pyplot as plt
from tensorflow.keras.regularizers import l1, l2
# Нормалізація даних
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((-1, 28, 28, 1))
x_test = x_test.reshape((-1, 28, 28, 1))
# Кодування міток у формат one-hotЫ
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential()
model.add(Conv2D(64, kernel_size=(3, 3), activation='ReLU', input_shape=(28, 28,1)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Conv2D(64, kernel_size=(3, 3), activation='ReLU')
#model.add(BatchNormalization())
#model.add(MaxPooling2D(pool_size=(2, 2)))
#model.add(Conv2D(64, kernel_size=(3, 3), activation='ReLU')
#model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(32, activation='ReLU'))
model.add(Flatten())
model.add(Dense(32, activation='ReLU'))
model.add(BatchNormalization())
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy',
metrics=['accuracy'])
history = model.fit(x_train, y_train, epochs=10, batch_size=256,
validation_data=(x_test, y_test))

loss, accuracy = model.evaluate(x_test, y_test)
print(f"Точність моделі: {accuracy*100:.2f}%")


# Виведення графіків втрат та точності
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Test Loss')
plt.legend()
plt.title('Loss Evolution')
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Test Accuracy')
plt.legend()
plt.title('Accuracy Evolution')
plt.tight_layout()
plt.show()


# Передбачення моделі на тестовому наборі
y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)
# Матриця помилок
conf_mtx = confusion_matrix(y_true, y_pred_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_mtx, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Розрахунок F1-оцінки, точності та відгуку
print('\nClassification Report:\n')
print(classification_report(y_true, y_pred_classes, digits=4))
