a1=int(input('перша зупинка першого автобусу: '))
while a1>100 or a1<1: 
    a1=int(input(' перша зупинка першого автобусу: '))
a2=int(input('кінцева зупинка першого автобусу: '))
while a2>100 or a2<1:
    a2=int(input('кінцева зупинка першого автобусу: '))
b1=int(input('перша зупинка другого автобусу: '))
while b1>100 or b1<1:
    b1=int(input(' перша зупинка другого автобусу: '))
b2=int(input('кінцева зупинка другого автобусу: '))
while b2>100 or b2<1:
    b2=int(input('кінцева зупинка другого автобусу: '))
    
A = {int(i) for i in range (a1,a2+1)}
if A == set():
    A = {int(i) for i in range (a2,a1+1)}
    
B = {int(l) for l in range (b1,b2+1)}
if B == set():
    B = {int(l) for l in range (b2,b1+1)}
    
print(len(set.intersection(A,B))) 
