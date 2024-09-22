def Fib(N):
 Fn_1,Fn_2 =1,1
 if N == 1 or N == 2:
    F = 1
 else:
    N-=2
    while N > 0:
     F=Fn_1 + Fn_2
     Fn_2 = Fn_1
     Fn_1 = F
     N-=1
 return F

N = int(input())
while N <= 0:
    N = int(input())
print('Число Фібоначчи:',Fib(N))

