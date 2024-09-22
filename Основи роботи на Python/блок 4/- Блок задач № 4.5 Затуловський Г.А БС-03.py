def for2(n):
    for x in range(n):
      lis.append(int(input()))
    print('максимальне число: ',max(lis))
    print('мінімальне число: ',min(lis))
    
def for3(n):
    for x in range(n):
      lis.append(int(input()))
    print('максимальне число: ',max(lis))
    print('мінімальне число: ',min(lis))
    
n = int(input('функція приймає 2 чи 3 числа? '))
while n<2 or n>3:
      n = int(input('функція приймає 2 чи 3 числа? ')) 
lis = []
if n == 2:
  for2(n)
else:
  for3(n)
