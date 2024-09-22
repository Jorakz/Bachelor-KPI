import math
def slog(n):
    k = 2
    while n!=k:
      if n%k==0:
        crat.append(k)
        n = n//k
      else:
        k+=1
    if n!=1:
        crat.append(n)
        
n= int(input('Введіть число: '))
crat=[]
slog(n)
print(n,'=', crat[0], end=' ',)
for x in range( len(crat)-1):
 print('*',crat[x+1],end=' ')
