N = int(input('Ввести целое положительное число: '))
if N < 0:
    while N<0:
     N = int(input('Ввести целое положительное число: '))
while N!=0:
    if N%2==0 and N%3!=0:
       print('two')
    elif N%2==0 and N%3==0:
       print('six')
    elif N%2!=0 and N%3==0:
       print('three')
    else:
       print('none')
    N = int(input('Ввести целое положительное число: '))
print('Finish')
