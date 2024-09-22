
import gzip
import idx2numpy
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Flatten, Dense, Dropout, Lambda
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt

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
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train = x_train[:15000, :, :]
x_test = x_test[:10000, :, :]
y_train = y_train[:15000]
y_test = y_test[:10000]
x_train /= 255.
x_test /= 255.

def create_base_model(input_shape):
    input = Input(shape=input_shape)
    x = Flatten()(input)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    x = Dropout(0.1)(x)
    x = Dense(128, activation='relu')(x)
    return Model(inputs=input, outputs=x)


base_model = create_base_model((28, 28))



def triplet_loss(y_true, y_pred, alpha = 0.4):
 total_lenght = y_pred.shape.as_list()[-1]
 anchor, positive, negative = y_pred[:,:int(total_lenght*1/3)], y_pred[:,int(total_lenght*1/3):int(total_lenght*2/3)], y_pred[:,int(total_lenght*2/3):]
 pos_dist = tf.reduce_sum(tf.square(anchor - positive), axis=-1)
 neg_dist = tf.reduce_sum(tf.square(anchor - negative), axis=-1)
 basic_loss = pos_dist - neg_dist + alpha
 loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
 return loss

anchor_input = Input((28,28), name='anchor_input')
positive_input = Input((28,28), name='positive_input')
negative_input = Input((28,28), name='negative_input')
anchor_embedding = base_model(anchor_input)
positive_embedding = base_model(positive_input)
negative_embedding = base_model(negative_input)
merged_vector = tf.keras.layers.concatenate([anchor_embedding,
positive_embedding, negative_embedding], axis=-1)
snn = Model(inputs=[anchor_input,positive_input, negative_input],
outputs=merged_vector)
snn.compile(optimizer=Adam(0.0001), loss=triplet_loss)

def create_base_model(input_shape):
 input = Input(shape=input_shape)
 x = Flatten()(input)
 x = Dense(128, activation='relu')(x)
 x = Dropout(0.1)(x)
 x = Dense(128, activation='relu')(x)
 x = Dropout(0.1)(x)
 x = Dense(128, activation='relu')(x)
 x = Dropout(0.1)(x)
 x = Dense(128, activation='relu')(x)
 x = Dropout(0.1)(x)
 x = Dense(128, activation='relu')(x)
 return Model(inputs=input, outputs=x)
base_model = create_base_model((28,28))

def triplet_loss(y_true, y_pred, alpha = 0.4):
 total_lenght = y_pred.shape.as_list()[-1]
 anchor, positive, negative = y_pred[:,:int(total_lenght*1/3)],y_pred[:,int(total_lenght*1/3):int(total_lenght*2/3)], y_pred[:,int(total_lenght*2/3):]
 pos_dist = tf.reduce_sum(tf.square(anchor - positive), axis=-1)
 neg_dist = tf.reduce_sum(tf.square(anchor - negative), axis=-1)
 basic_loss = pos_dist - neg_dist + alpha
 loss = tf.reduce_sum(tf.maximum(basic_loss, 0.0))
 return loss

anchor_input = Input((28,28), name='anchor_input')
positive_input = Input((28,28), name='positive_input')
negative_input = Input((28,28), name='negative_input')
anchor_embedding = base_model(anchor_input)
positive_embedding = base_model(positive_input)
negative_embedding = base_model(negative_input)
merged_vector = tf.keras.layers.concatenate([anchor_embedding,
positive_embedding, negative_embedding], axis=-1)
snn = Model(inputs=[anchor_input,positive_input, negative_input],
outputs=merged_vector)
snn.compile(optimizer=Adam(0.0001), loss=triplet_loss)

def compute_accuracy(y_true, y_pred):
 anchor, positive, negative = y_pred[:, :128], y_pred[:, 128:256], y_pred[:, 256:]
 pos_dist = np.sum(np.square(anchor - positive), axis=1)
 neg_dist = np.sum(np.square(anchor - negative), axis=1)
 return np.mean(pos_dist < neg_dist)
def get_triplets(data, labels):
    anchor_images = np.array([]).reshape((-1, 28, 28))
    positive_images = np.array([]).reshape((-1, 28, 28))
    negative_images = np.array([]).reshape((-1, 28, 28))

    unique_labels = np.unique(labels)
    for label in unique_labels:
        same_class = data[labels == label]
    diff_class = data[labels != label]

    for anchor_img in same_class:
        for _ in range(2):  # Just take two triplets per anchor image for simplicity
            positive_img = same_class[np.random.randint(len(same_class))]
            negative_img = diff_class[np.random.randint(len(diff_class))]
            anchor_images = np.vstack([anchor_images, np.expand_dims(anchor_img, axis=0)])
            positive_images = np.vstack([positive_images, np.expand_dims(positive_img, axis=0)])
            negative_images = np.vstack([negative_images, np.expand_dims(negative_img, axis=0)])
    return [anchor_images, positive_images, negative_images]


triplet_train = get_triplets(x_train, y_train)
triplet_test = get_triplets(x_test, y_test)
history = snn.fit(triplet_train, np.zeros(len(triplet_train[0])), epochs=20,batch_size=4, validation_data=(triplet_test, np.zeros(len(triplet_test[0]))))

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper right')
plt.show()
anchor_embeddings = base_model.predict(triplet_test[0])
positive_embeddings = base_model.predict(triplet_test[1])
negative_embeddings = base_model.predict(triplet_test[2])

# Computing the distances
pos_dist = np.sum(np.square(anchor_embeddings - positive_embeddings), axis=1)
neg_dist = np.sum(np.square(anchor_embeddings - negative_embeddings), axis=1)

# Accuracy computation
accuracy = np.sum(pos_dist < neg_dist) / len(pos_dist)
print(f"Accuracy: {accuracy * 100:.2f}%")
