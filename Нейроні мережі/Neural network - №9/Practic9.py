import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from scipy.io import loadmat
from keras.applications import VGG16
import matplotlib.pyplot as plt
from keras import backend as K
from keras.models import Model
from keras.layers import Dense, Flatten


# Завантаження датасету SVHN
def load_svhn_data():
    svhn_train = loadmat('train_32x32.mat')
    images_train = svhn_train['X']
    labels_train = svhn_train['y']
    svhn_test = loadmat('test_32x32.mat')
    images_test = svhn_test['X']
    labels_test = svhn_test['y']
    # Заміна міток 10 на 0
    labels_test[labels_test == 10] = 0
    labels_train[labels_train == 10] = 0



    return images_train, labels_train,images_test, labels_test





# Дослідження розподілу класів та кількості зображень
def explore_data(labels,l):
    class_distribution = pd.Series(labels.flatten()).value_counts().sort_index()
    print("Розподіл класів:")
    print(class_distribution)
    plt.title(l)
    plt.bar(class_distribution.index, class_distribution.values)
    plt.xlabel('Клас')
    plt.ylabel('Кількість зображень')
    plt.show()

# Попередня обробка даних
def preprocess_data(x_train, y_train, x_test , y_test):
    # Масштабування значень пікселів в діапазон [0, 1]
    x_train = images_train.astype('float32')  / 255.0
    x_test = images_test.astype('float32')  / 255.0


    # Кодування міток у формат one-hot
    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    # Аугментація даних
    datagen = ImageDataGenerator(rotation_range=10, width_shift_range=0.1, height_shift_range=0.1, zoom_range=0.1)



    return x_train, x_test, y_train, y_test, datagen

# Завантаження та дослідження даних
images_train, labels_train,images_test, labels_test = load_svhn_data()





print('train_32x32.mat')
explore_data(labels_train,'Розподіл класів у тренувальній вибірці train_32x32.mat')
print(' ')
print('test_32x32.mat')
explore_data(labels_test,'Розподіл класів у тестовій вибірці test_32x32.mat')
# Попередня обробка даних
x_train, x_test, y_train, y_test, datagen = preprocess_data(images_train, labels_train,images_test, labels_test)


print('Розмір y train -',len(y_train))
print('Розмір x train -',len(x_train[0][0][0]))

print('Розмір y test -',len(y_test))
print('Розмір x test -',len(x_test[0][0][0]))
print(' ')
x_train = np.moveaxis(x_train, -1, 0)
x_test = np.moveaxis(x_test, -1, 0)



x_train = x_train[:30000]
x_test = x_test[:5000]
y_train = y_train[:30000]
y_test = y_test[:5000]
# Обчислення кількості елементів в кожному класі
print('Вміст тренувальній вибірці:')
class_counts = np.sum(y_train, axis=0)
for class_index, count in enumerate(class_counts):
    print(f"{class_index}    {count} ")
print(' ')
print('Вміст тестової вибірці:')
class_counts = np.sum(y_test, axis=0)
for class_index, count in enumerate(class_counts):
    print(f"{class_index}    {count} ")

class_counts_train = np.sum(y_train, axis=0)


plt.bar(range(10), class_counts_train, tick_label=range(10))
plt.xlabel('Клас')
plt.ylabel('Кількість зображень')
plt.title('Розподіл класів у тренувальній вибірці')
plt.show()


class_counts_test = np.sum(y_test, axis=0)
plt.bar(range(10), class_counts_test, tick_label=range(10))
plt.xlabel('Клас')
plt.ylabel('Кількість зображень')
plt.title('Розподіл класів у тестовій вибірці')
plt.show()
print('Розмір y train -',len(y_train))
print('Розмір x train -',len(x_train))

print('Розмір y test -',len(y_test))
print('Розмір y test -',len(x_test))


base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))

# Додавання нових верхніх шарів
x = base_model.output
x = Flatten()(x)
x = Dense(512, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)
# З'єднання базової моделі та нових верхніх шарів
model = Model(inputs=base_model.input, outputs=predictions)
# Заморожування ваг базової моделі
for layer in base_model.layers:
 layer.trainable = False
# Компіляція моделі



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


model.compile(optimizer='adam', loss='categorical_crossentropy',
              metrics=['accuracy', precision, recall, f1_score])
history = model.fit(datagen.flow(x_train, y_train,  batch_size=32),epochs=10,validation_data=(x_test, y_test) )
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

print(f"Точність на тестовому наборі: {history.history['val_accuracy'][-1]*100:.2f}%")
print(f"Precision на тестовому наборі: {history.history['val_precision'][-1]*100:.2f}%")
print(f"Recall на тестовому наборі: {history.history['val_recall'][-1]*100:.2f}%")
print(f"F1-score на тестовому наборі: {history.history['val_f1_score'][-1]*100:.2f}%")
