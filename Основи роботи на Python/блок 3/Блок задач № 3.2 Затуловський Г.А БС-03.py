import math
def fx(x):
  f = math.sin(x)/ x
  print(x,' -> ',f)
  return f

n = int(input())
liste={}
while n <= 0:
    n = int(input())
x =int(input())    
f = fx(x)
liste[x] = f
n = n - 2
while n >= 0:
    n-=1
    x = int(input())
    if x in liste.keys():
      print('Повторне виведення',x ,'->',liste.get(x))
    else:
      liste[x] = fx(x)


     
    
