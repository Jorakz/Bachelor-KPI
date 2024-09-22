def ran(m):
    """Функція заповнює матрицю випадковими числами"""
    import random
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j]=(random.randint(a,b))
    return m

def summ(m):
    """Функція яка знаходить значення суми елементів квадратної матриці, які розташовані нижче головної матриці"""
    s=0
    n=1
    f=n
    for i in range(1,len(m)):
        while n > 0:
          s = s + m[i][n-1]
          n-=1
        n=f+1
        f=n
    return s
   
N = int(input('Кількість матриць: '))
while N <= 0:
 N = int(input('Кількість матриць: ')) 
maxim = 0
for x in range (N):
    ij = int(input('Квадратна матриця розміром: '))
    a = int(input('Мінімальний елемент: '))
    b = int(input('Максимальний елемент: '))
    while b <= a:
      b = int(input('Максимальний елемент: '))
    m = [0]* ij
    for i in range(ij):
      m[i] = [0]*ij    
    m =  ran(m)
    for i in range(len(m)):
        for j in range(len(m[i])):
          print(m[i][j],end=' ')
        print(' ')
    s=summ(m)
    while maxim < s:
        maxim = s
print('Максимальна значення суми елементів квадритних матриці, які розташовані нижче головної діагоналі серед матриць:',maxim)
print('')
help(summ)
help(ran)

