a = float(input('Введіть a:' ))
x = float(input('Введіть x:' ))
if x > a:
 y =(abs(x**2 - a))**(1/3) + x**2
elif x < a:
 y = (a - x**2)**3 + x**2
else:
  y = (a + x**2)**2 + x**3
print('y = ', round(y,10))  
