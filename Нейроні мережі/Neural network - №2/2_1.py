import numpy as np
import matplotlib.pyplot as plt
# ініціалізація послідовності випадкових чисел
np.random.seed(42)
# створюємо np-масив з 1000 випадкових чисел в діапазоні 0..1
sz = 1000
x = np.random.rand(sz, 1)
# будуємо функцію y = f(x) та додаємо трохи гаусового шуму
y = x**(1/2) + np.random.normal(loc=0.0, scale=0.1, size=x.shape)


# формуємо індекси від 0 до 999
idx = np.arange(sz)
# випадково перемішуємо
np.random.shuffle(idx)
train_idx = idx
# формуємо набори навчальних даних
x_train, y_train = x[train_idx], y[train_idx]

plt.plot(x_train, y_train)
plt.axis([0, 1 , 0, 1])
plt.show()

# Встановлюємо початкові випадкові значення коефіцієнтів лінійної регресії
a = np.random.randn(1)
b = np.random.randn(1)
print(a, b)
# розрахунок початкової помилки (середньоквадратична функція помилки)
initial_error = ((y_train - (a + b * x_train)) ** 2).mean()

print(f"Початкова помилка: {initial_error}")
# швидкість навчання
lr = 0.1
# кількість епох
n_epochs = 100000
# основний цикл
for epoch in range(n_epochs):
    # обчислюємо отриманий масив з коефіцієнтами A і B
    # На основі тренувального зразка
    yhat = a + b * x_train

    # 1. Визначаємо втрати
    # розглядаємо відхилення нового результату:
    error = (y_train - yhat)

    # 2. Рахуємо градієнти (за формулою похідної)
    # для коефіцієнта a
    a_grad = -2 * error.mean()
    # для коефіцієнта b
    b_grad = -2 * (x_train * error).mean()

    # 3. оновлюємо параметри, використовуючи коефіцієнт швидкості навчання
    old_error =((y_train - (a + b * x_train)) ** 2).mean()
    a = a - lr * a_grad
    b = b - lr * b_grad

print(a, b)
# розрахунок помилки після оптимізації
final_error = ((y_train - (a + b * x_train)) ** 2).mean()

print(f"Кінцева помилка: {final_error}")

print(f"Кількість ітерацій: {n_epochs}")
print(f"швидкість навчання: {lr}")
