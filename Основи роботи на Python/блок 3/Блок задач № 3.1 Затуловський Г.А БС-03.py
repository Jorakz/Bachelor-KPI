mas = []
while True:
    n = str(input()) 
    if n == 'end':
        break
    mas.append([int(s) for s in n.split()]) 
I = len(mas) 
J = len(mas[0])
mas2 = [[sum([mas[i-1][j], mas[(i+1)%I][j], mas[i][j-1], mas[i][(j+1)%J]]) for j in range(J)] for i in range(I)]

for i in range (I):
    for j in range (J):
        print(mas2[i][j], end =' ')
    print()

