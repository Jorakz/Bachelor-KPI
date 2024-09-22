import numpy as np
np.random.seed(42)
sz = 1000
x = np.random.rand(sz, 1)
y = x**(1/2) + np.random.normal(loc=0.0, scale=0.1, size=x.shape)
idx = np.arange(sz)
np.random.shuffle(idx)
x_train, y_train = x[idx], y[idx]
# початкові випадкові значення для a і b
a_initial = np.random.randn(1)
b_initial = np.random.randn(1)
print(a_initial, b_initial)
# розрахунок початкової помилки
initial_error = ((y_train - (a_initial + b_initial * x_train)) ** 2).mean()
print(f"Початкова помилка: {initial_error}")
population_size = 10000
num_generations = 1000
mutation_rate = 0.1
# Створюємо початкову популяцію
population = np.random.randn(population_size, 2)
for _ in range(num_generations):
 # Обчислюємо помилку для кожного індивіда в популяції
 errors = np.array([((y_train - (a + b * x_train)) ** 2).mean() for a, b in population])
 # Вибираємо найкращих індивідів (тих, у кого помилка найменша)
 fitness_scores = 1 / (1 + errors)
 probs = fitness_scores / fitness_scores.sum()
 selected = population[np.random.choice(np.arange(population_size),size=population_size, replace=True, p=probs)]
 # Створюємо нове покоління через схрещування
 pairs = selected[np.random.randint(0, population_size, size=(population_size, 2))]
 new_population = pairs.mean(axis=1)
 # Застосовуємо мутації
 mutations = (np.random.rand(population_size, 2) - 0.5) * mutation_rate
 new_population += mutations
 # Замінюємо стару популяцію новою
 population = new_population

# Вибираємо найкраще рішення з кінцевої популяції
best_idx = np.argmin([((y_train - (a + b * x_train)) ** 2).mean() for a, b in population])
best_a, best_b = population[best_idx]
print(f'[{best_a}],[{best_b}]')
# розрахунок помилки після оптимізації
final_error = ((y_train - (best_a + best_b * x_train)) ** 2).mean()
print(f"Кінцева помилка: {final_error}")
print(f"Кількість ітерацій: {num_generations}")
print(f"Розмір популяції: {population_size}")
print(f"Коефіцієнт мутації: {mutation_rate}")
