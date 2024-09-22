def sov():
    summ=0
    for x in range(1,10000):
        for y in range(1,x): 
            if x%y==0:
                summ+=y
        if summ==x:
            print(x)
        summ=0
print('Cовершенные числа в диапазоне от 1 до 100 000:')
sov()
