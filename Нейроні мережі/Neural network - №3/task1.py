from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn import datasets
import openpyxl as op
import pandas as pd
import matplotlib.pyplot as plt
# load data
dataset = pd.read_excel('diabetes.xlsx')

X= dataset.iloc[:, :8].to_numpy()
Y= dataset.iloc[:, 8].to_numpy()
norm = StandardScaler()
X = norm.fit_transform(X)

Y = Y.reshape(-1,1)
X=np.array(X)
Y=np.array(Y)

# Визначаємо структуру мережі
n_input = 8
n_hidden = 768
n_output = 1
# Ваги та зміщення для першого шару (вхідний -> прихований)
W1 = np.random.randn(n_input, n_hidden)
b1 = np.zeros((1, n_hidden))
# Ваги та зміщення для другого шару (прихований -> вихідний)
W2 = np.random.randn(n_hidden, n_output)
b2 = np.zeros((1, n_output))

def sigmoid(x):
 return 1 / (1 + np.exp(-x))
def sigmoid_derivative(x):
 return x * (1 - x)
# Прямий прохід
def Softmax(x):
 e_x = np.exp(x - np.max(x))  # Subtracting max(x) for numerical stability
 return e_x / e_x.sum()
def Softmax_derivative(x):
 s = Softmax(x)
 return s * (1 - s)
def forward_pass(X):
 Z1 = np.dot(X, W1) + b1
 A1 = sigmoid(Z1)#Softmax(Z1)
 Z2 = np.dot(A1, W2) + b2
 A2 = sigmoid(Z2)#Softmax(Z2)
 return Z1, A1, Z2, A2
# Градієнтний спуск та зворотній прохід
def backward_pass(X, Y, Z1, A1, Z2, A2, W1, b1, W2, b2, learning_rate=0.01):
 m = X.shape[0]
 dZ2 = A2 - Y
 dW2 = 1/m * np.dot(A1.T, dZ2)
 db2 = np.sum(dZ2, axis=0, keepdims=True)
 dA1 = np.dot(dZ2, W2.T)
 dZ1 = dA1 * sigmoid_derivative(A1)#Softmax_derivative(A1)
 dW1 = 1/m * np.dot(X.T, dZ1)
 db1 = np.sum(dZ1, axis=0, keepdims=True)
 W2 -= learning_rate * dW2
 b2 -= learning_rate * db2
 W1 -= learning_rate * dW1
 b1 -= learning_rate * db1

 return W1, b1, W2, b2
def compute_loss(Y, predictions):
 m = Y.shape[0]

 loss = -np.mean(Y * np.log(predictions) + (1 - Y) * np.log(1 - predictions))

 return loss

# Тренування моделі
def train_model(X, Y, W1, b1, W2, b2, num_iterations=1000):
 loss_values =[]
 for i in range(num_iterations+1):
    Z1, A1, Z2, A2 = forward_pass(X)
    loss = compute_loss(Y,A2)
    loss_values.append(loss)
    print(f'Iteration {i}, loss = {loss}')
    W1, b1, W2, b2 = backward_pass(X, Y, Z1, A1, Z2, A2, W1, b1, W2, b2)

 return W1, b1, W2, b2, loss_values

W1, b1, W2, b2, loss = train_model(X, Y, W1, b1, W2, b2, num_iterations=1000)
_,_,_,predictions = forward_pass(X)
predictions = (predictions > 0.5).astype(int)

accuracy = np.mean(predictions == Y)

print("Нейронну мережа - Accuracy:", accuracy)
plt.plot(loss)
plt.xlabel('Iterations')
plt.ylabel('Loss')
plt.title('Training Loss over Time')
plt.show()

from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report
clf = MLPClassifier(hidden_layer_sizes=(n_hidden,), max_iter=1000, alpha=0.01, solver='sgd', verbose=10, random_state=42, learning_rate_init=.01)
clf.fit(X, Y.ravel())

# MLPClassifier з sklearn
Y_iris_pred_sklearn = clf.predict(X)

accuracy = np.mean(Y_iris_pred_sklearn == Y)
print("MLPClassifier - Accuracy:", accuracy)
