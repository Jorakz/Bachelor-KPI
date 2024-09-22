print('Проверить условие: ровно одно из чисел a, b, c положительное.')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a > 0 and b <= 0 and c <= 0 or b > 0 and a <= 0 and c <= 0 or c >0 and b <= 0 and a <= 0:
  print('YES')
else:
  print('NO')
