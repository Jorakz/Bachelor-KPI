import numpy as np
np.random.seed(42)
sz = 1000
x = np.random.rand(sz, 1)
y = x**(1/2) + np.random.normal(loc=0.0, scale=0.1, size=x.shape)
idx = np.arange(sz)
np.random.shuffle(idx)
x_train, y_train = x[idx], y[idx]
# Задаємо початкові параметри
a = np.random.randn(1)
b = np.random.randn(1)
print(a,b)
# розрахунок помилки на початку
initial_error  = ((y_train - (a + b * x_train)) ** 2).mean()
print(f"Початкова помилка: {initial_error }")
# Визначаємо крок (можливо, потрібно налаштувати)
step_size = 0.05
# Визначаємо кількість ітерацій
num_iters = 100000
for _ in range(num_iters):
 # Спробуємо змінити 'a' трохи
 a_new = a + (np.random.rand() - 0.5) * step_size
 b_new = b + (np.random.rand() - 0.5) * step_size
 # Обчислюємо помилку для старого та нового 'a'
 old_error = ((y_train - (a + b * x_train)) ** 2).mean()
 new_error = ((y_train - (a_new + b_new * x_train)) ** 2).mean()
 # Якщо нова помилка менша, оновлюємо 'a' та 'b'
 if new_error < old_error:
  a, b = a_new, b_new

print(a, b)
# розрахунок помилки після оптимізації
final_error = ((y_train - (a + b * x_train)) ** 2).mean()
print(f"Кінцева помилка: {final_error}")
print(f"Кількість ітерацій: {num_iters}")
print(f"Визначений крок: {step_size}")