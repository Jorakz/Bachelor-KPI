import random 
n = int(input('кількість рядків n = '))
m = int(input('кількість стовпців m = '))
a = int(input('a = '))
b = int(input('b = '))
if a>b:
   b = int(input('b = '))
Sp = []
Sp = [[int(random.uniform(a,b+1)) for j in range(m)] for i in range(n)]
for row in Sp:
    for elem in row:
        print(elem,end=' ')
    print()
print('двовимірний масив : ', Sp)
Sp1=[]
for row in Sp:
    s = 0
    for elem in row:			
        s += elem
    Sp1.append(s)
print('сума елементів у кожному рядку в одномірному масиві = ',Sp1)

