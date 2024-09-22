s = str(input('Введите 6 цифр - '))
a = list(s)
while len(a)!=6:
    s = str(input('Введіть 6 цифр - '))
    a = list(s)
b = [int(b) for b in a]
sum1=0
sum2=0
m=0
for m in range(len(b)):
    if m<=2:
      sum1+=b[m]
for m in range(len(b)):
    if m>2:
       sum2+=b[m]
if sum1==sum2:
    print('Счастливый')
else:
    print('Обычный')
