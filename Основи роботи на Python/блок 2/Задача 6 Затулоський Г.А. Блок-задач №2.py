summa = 0
x = 0
for i in range(1000,10000):
    L =str(i)
    for a in range(4):
        summa += int(L[a])
    if summa == 15:
       if x % 15 == 0:
            print('')
       print(i,end = ' ')
       x+=1
    summa = 0
    
