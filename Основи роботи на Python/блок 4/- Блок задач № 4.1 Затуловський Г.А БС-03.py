def f(n):
    count=0
    for x in n:
        lis.append(x)
        a =''
    count=len(lis)
    lis.reverse()
    print(*lis,sep=',',end='')
    print( '',' Number of digits = ',sep=';',end='')
    print(count)
n = input()
lis = []
f(n)
