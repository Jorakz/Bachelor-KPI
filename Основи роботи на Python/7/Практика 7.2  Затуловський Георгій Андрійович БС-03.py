import random 
n=int(input('введіть n = ')) 
a=int(input('введіть a = '))
b=int(input('введіть b = '))
while b<=a:
      b=int(input('введіть b = '))
lst=[] 
for i in range(n): 
    lst.append(random.randint(a,b))
print(lst)
mini=lst[0]            # знайдення мінімального елемента списка 
ind=0 
for i in range(1,n): 
    if lst[i]<mini: 
        mini=lst[i] 
        ind=i 
print('мінімальний елемент списку = ', mini, sep='')
for i in range(n):     # Обчислити cуму елементів списку, розташованих між
    if lst[i]>0:       # першим і останнім додатними елементами
        dot1=i 
        break
for i in range(n-1,-1,-1): 
    if lst[i]>0: 
        dot2=i 
        break
suma=0
for i in range(dot1+1,dot2):
      suma+=lst[i]
print ('сума елементів списку = ',suma)

