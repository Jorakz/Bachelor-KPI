import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style= "darkgrid", color_codes = True)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout, Input
from keras.regularizers import l2
from tensorflow.keras.metrics import Precision, Recall, BinaryAccuracy
from sklearn.metrics import roc_curve, auc
from tensorflow.keras.preprocessing.image import load_img
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings('ignore')
from keras import backend as K


train = keras.utils.image_dataset_from_directory(
    directory='chest_xray/train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(256, 256))

validation = keras.utils.image_dataset_from_directory(
    directory='chest_xray/val',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(256, 256))

test = keras.utils.image_dataset_from_directory(
    directory='chest_xray/test',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(256, 256))

x_train = []
y_train = []
x_val = []
y_val = []
x_test = []
y_test = []

for feature, label in train:
    x_train.append(feature.numpy())
    y_train.append(label.numpy())

for feature, label in test:
    x_test.append(feature.numpy())
    y_test.append(label.numpy())

for feature, label in validation:
    x_val.append(feature.numpy())
    y_val.append(label.numpy())

x_train = np.concatenate(x_train, axis=0)
x_val = np.concatenate(x_val, axis=0)
x_test = np.concatenate(x_test, axis=0)
y_train = np.concatenate(y_train, axis=0)
y_val = np.concatenate(y_val, axis=0)
y_test = np.concatenate(y_test, axis=0)
x_train, _, y_train, _ = train_test_split(x_train,y_train,train_size=0.9, shuffle=True, random_state=42)
x_train = x_train[:1500]
y_train = y_train[:1500]
print("x_train:", x_train.shape)
print("y_train:", y_train.shape)
print("x_val:", x_val.shape)
print("y_val:", y_val.shape)
print("x_test:", x_test.shape)
print("y_test:", y_test.shape)

def precision(y_true, y_pred):

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision


def recall(y_true, y_pred):

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall


def f1_score(y_true, y_pred):
    precision_val = precision(y_true, y_pred)
    recall_val = recall(y_true, y_pred)
    return 2 * ((precision_val * recall_val) / (precision_val + recall_val + K.epsilon()))


x_train=x_train/256
x_val=x_val/256
x_test=x_test/256

from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
model = Sequential()
model.add(Input(shape=(256, 256, 3)))
model.add(Dense(32, activation='relu'))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.02)))
model.add(Dropout(0.1))
model.add(Dense(2, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy', precision, recall, f1_score])



history = model.fit(x_train, y_train,  batch_size=64,epochs=10,validation_data=(x_test, y_test))
# Графік точності
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Точність моделі')
plt.ylabel('Точність')
plt.xlabel('Епоха')
plt.legend(['Навчання', 'Тест'], loc='upper left')
plt.show()
# Графік функції втрат
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Функція втрат')
plt.ylabel('Втрати')
plt.xlabel('Епоха')
plt.legend(['Навчання', 'Тест'], loc='upper left')
plt.show()
from sklearn.metrics import confusion_matrix, classification_report
import seaborn as sns

y_pred = model.predict(x_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)
y_test = np.argmax(y_test, axis=1)
y_test = y_test.astype(int)

print('Predicted y: \n',y_pred_classes)
print('True y: \n',y_test)
conf_mtx = confusion_matrix(y_test,y_pred_classes)
plt.figure(figsize=(10,8))
sns.heatmap(conf_mtx, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()
# Розрахунок F1-оцінки, точності та відгуку
print('\nClassification Report:\n')
print(classification_report(y_test, y_pred_classes, digits=4))
