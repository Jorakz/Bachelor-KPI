a=int(input('Відстань між рядами дорівнює: '))
while a<=0:
    a=int(input('Відстань між рядами дорівнює: '))
b=int(input('Відстань між дірочками в ряду: '))
while b<=0:
    b=int(input('Відстань між дірочками в ряду: '))
l=int(input('Довжина вільного кінця шнурка: '))
while l<=0:
    l=int(input('Довжина вільного кінця шнурка: '))
N=int(input('Кількість дірочок в кожному ряду: '))
while N<=0:
    N=int(input('Кількість дірочок в кожному ряду: '))
if N==1:
    length = l*2+a
else:
    length=2*l+a+N*2*(a**2+b**2)**(1/2)
print('Довжина шнура: ', round(length,0))
