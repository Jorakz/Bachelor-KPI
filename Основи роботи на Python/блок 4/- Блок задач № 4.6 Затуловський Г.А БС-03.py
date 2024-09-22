def game(x):
  from random import randint
  x=randint(1,100)
  return x


def p(N,x,gg):
 while N>0:
    k = int(input())
    if x < k:
           print('Загаданное число меньше:',k)
    elif x > k:
           print('Загаданное число больше ',k) 
    else :
        gg+=1
        break
    N-=1
 return gg
   
N = 10
x=0
gg=0
x = game(x)
gg = p(N,x,gg)

if gg == 1:
    print('Вы выграли, загаданным числом было:',x)
else:
    print('Вы проиграли, загаданным числом было:',x)
