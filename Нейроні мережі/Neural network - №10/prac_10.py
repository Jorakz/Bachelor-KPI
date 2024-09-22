import zipfile
import pandas as pd
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Flatten, Dropout, LSTM, Embedding, Bidirectional, BatchNormalization
import matplotlib.pyplot as plt
from tensorflow.keras.regularizers import l1, l2
with zipfile.ZipFile('train.tsv.zip', 'r') as zip_ref:
    zip_ref.extractall('data')

with zipfile.ZipFile('test.tsv.zip', 'r') as zip_ref:
    zip_ref.extractall('data')

train_data = pd.read_csv('data/train.tsv', sep='\t')
test_data = pd.read_csv('data/test.tsv', sep='\t')

print('\ntrain \n',train_data.head())
print('\n\ntest \n',test_data.head())
print('\n\ntrain \n' ,train_data.info())
print('\n\ntest \n' ,test_data.info())
print('\n\ntrain \n' ,train_data.shape)
print('\n\ntest \n' ,test_data.shape)
val_array = train_data['Sentiment'].value_counts()
plt.bar(val_array.index, val_array)
plt.title('train.tsv - count sentiments')
plt.xlabel('review rating/Sentiments')
plt.ylabel('No of reviews')
plt.show()

train_data['Word_Count'] = train_data['Phrase'].apply(lambda x: len(str(x).split()))
plt.hist(train_data['Word_Count'], bins=20, edgecolor='black')
plt.title('Distribution of Word Counts in Phrases')
plt.xlabel('Word Count')
plt.ylabel('Frequency')
plt.show()

common_words = pd.Series(' '.join(train_data['Phrase']).split()).value_counts()[:10]
print("Common Words:\n\n", common_words)


x = train_data['Phrase']
y = train_data['Sentiment']
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state=42 )


print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)
from keras.preprocessing.text import Tokenizer
tokenize = Tokenizer(num_words=2000,lower=True)
tokenize.fit_on_texts(x_train)
x_train = tokenize.texts_to_sequences(x_train)
x_test= tokenize.texts_to_sequences(x_test)

x_train = pad_sequences(x_train, maxlen=50)
x_test = pad_sequences(x_test, maxlen=50)


from keras.utils import to_categorical
num_classes = 5
y_train = to_categorical(y_train,num_classes)
y_test = to_categorical(y_test,num_classes)
print(y_train.shape)
print(x_train.shape)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, SimpleRNN
model = Sequential()
model.add(Embedding(2000, 32))
#model.add(SimpleRNN(32, return_sequences=True))

model.add(LSTM(32, return_sequences=True))
model.add(Dropout(0.1))
#model.add(SimpleRNN(32))
#model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dense(32, activation='relu'))
model.add(LSTM(32))
model.add(Dropout(0.1))
#model.add(Dense(32, activation='relu', kernel_regularizer=l1(0.001)))
model.add(Dense(32, activation='relu'))
model.add(Dense(5, activation='sigmoid'))

model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])
history = model.fit(x_train, y_train, epochs=10, batch_size=128, validation_split=0.2)

import matplotlib.pyplot as plt
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(acc) + 1)
plt.plot(epochs, acc, 'bo', label='Training acc')
plt.plot(epochs, val_acc, 'b', label='Validation acc')
plt.title('Training and validation accuracy')
plt.legend()
plt.figure()
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.show()
from sklearn.metrics import precision_score, recall_score, f1_score
y_pred = model.predict(x_test)
y_test = (y_test > 0.5).astype(int).flatten()
y_pred = (y_pred > 0.5).astype(int).flatten()

precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
