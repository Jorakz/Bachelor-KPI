n = int(input('Введіть значення n: ' ))
summa = 0
for i in range(n):
  summa = summa + (i**2 + 3*i)**(1/2) - i
print('Сумма:',summa)
