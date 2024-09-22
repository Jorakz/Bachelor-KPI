a = 1000
b = float(input('Введите b: '))
y = ((a - b)**3 - a**3) / (b**3 - 3 * a * b**2 - 3 * a**2 * b)
print('y = ', round(y,10))
