x = float(input('спортсмен пробежал в первый день: '))
while x <= 0:
     x = float(input('спортсмен пробежал в первый день: '))
y = float(input('Растояние в км: '))
while y <= 0:
     y = float(input('Растояние в км: '))
days = 1
while x < y:
     x = x*1.1
     days += 1
print(days)
