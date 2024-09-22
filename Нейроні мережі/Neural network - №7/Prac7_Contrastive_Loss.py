import gzip
import idx2numpy
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout, Lambda,Conv2D, MaxPooling2D, BatchNormalization
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
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))


def create_pairs(x, digit_indices):
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(10)]) - 1
    for d in range(10):
        for i in range(n):
            z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
            pairs += [[x[z1], x[z2]]]
            inc = np.random.randint(1, 10)
            dn = (d + inc) % 10
            z1, z2 = digit_indices[d][i], digit_indices[dn][i]
            pairs += [[x[z1], x[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels)


digit_indices = [np.where(y_train == i)[0] for i in range(10)]
tr_pairs, tr_y = create_pairs(x_train, digit_indices)

digit_indices = [np.where(y_test == i)[0] for i in range(10)]
te_pairs, te_y = create_pairs(x_test, digit_indices)



def create_base_network(input_shape):
    input = Input(shape=input_shape)
    x = Flatten()(input)
    #x = Dense(128, activation='relu', kernel_regularizer=l2(0.01),input_shape=(10,))(x)
    x = Dense(128, activation='relu')(x)
    #x = BatchNormalization()(x)
    x = Dropout(0.1)(x)
    #x = Dense(128, activation='relu', kernel_regularizer=l1(0.001),input_shape=(10,))(x)
    x = Dense(128, activation='relu')(x)
    #x = BatchNormalization()(x)
    #x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    #x = Dense(128, activation='relu')(x)
    #x = Conv2D(32, kernel_size=(3, 3), activation='relu')(input)
    #x = MaxPooling2D(pool_size=(2, 2))(x)
    #x = Flatten()(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)




    return Model(input, x)

base_network = create_base_network([28, 28, 1])
input_a = Input(shape=(28, 28, 1))
input_b = Input(shape=(28, 28, 1))

processed_a = base_network(input_a)
processed_b = base_network(input_b)


def euclidean_distance(vects):
    x, y = vects
    sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
    return K.sqrt(K.maximum(sum_square, K.epsilon()))


distance = Lambda(euclidean_distance)([processed_a, processed_b])
model = Model([input_a, input_b], distance)


def contrastive_loss(y_true, y_pred):
    margin = 1
    y_true = K.cast(y_true, 'float32')
    sqaure_pred = K.square(y_pred)
    margin_square = K.square(K.maximum(margin - y_pred, 0))
    return K.mean(y_true * sqaure_pred + (1 - y_true) * margin_square)

model.compile(loss=contrastive_loss, optimizer=RMSprop())
history = model.fit([tr_pairs[:, 0], tr_pairs[:, 1]], tr_y, epochs=20, batch_size=128,validation_data=([te_pairs[:, 0], te_pairs[:, 1]], te_y))
predicted = model.predict([te_pairs[:, 0], te_pairs[:, 1]])

# 'history' - це історія, яка повертається після навчання моделі
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper left')
plt.show()
threshold = 0.5
binary_predictions = [1 if dist < threshold else 0 for dist in predicted]
accuracy = accuracy_score(te_y, binary_predictions)
precision = precision_score(te_y, binary_predictions)
recall = recall_score(te_y, binary_predictions)
f1 = f1_score(te_y, binary_predictions)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")