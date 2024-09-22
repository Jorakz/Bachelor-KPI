a1=int(input('перша зупинка першого автобусу: '))
while a1>100 or a1<1: 
    a1=int(input(' перша зупинка першого автобусу: '))
a2=int(input('кінцева зупинка першого автобусу: '))
while a2>100 or a2<1:
    a2=int(input('кінцева зупинка першого автобусу: '))
b1=int(input('перша зупинка другого автобусу: '))
while b1>100 or b1<1:
    b1=int(input(' перша зупинка другого автобусу: '))
b2=int(input('кінцева зупинка другого автобусу: '))
while b2>100 or b2<1:
    b2=int(input('кінцева зупинка другого автобусу: '))
p=0
if a1<a2 and b1<b2 and a1<=b1:
   while a1<=a2 and b1<=b2:
     if a1==b1:
      a1+=1
      b1+=1
      p+=1
     else:
      a1+=1
elif a1<a2 and b1<b2 and a1>=b1:
   while a1<=a2 and b1<=b2:
     if a1==b1:
      a1+=1
      b1+=1
      p+=1
     else:
      b1+=1
elif a1<a2 and b2<b1 and a1<=b2:
   while a1<=a2 and b2<=b1:
     if a1==b2:
      a1+=1
      b2+=1
      p+=1
     else:
      a1+=1
elif a1<a2 and b2<b1 and a1>=b2:
   while a1<=a2 and b2<=b1:
     if a1==b2:
      a1+=1
      b2+=1
      p+=1
     else:
      b2+=1
elif a1>a2 and b2<b1 and a2<=b2:
   while a1>=a2 and b2<=b1:
     if a2==b2:
      a2+=1
      b2+=1
      p+=1
     else:
      a2+=1
elif a1>a2 and b2<b1 and a2>=b2:
   while a1>=a2 and b2<=b1:
     if a2==b2:
      a2+=1
      b2+=1
      p+=1
     else:
      b2+=1
elif a1>a2 and b2>b1 and b1>=a2:
   while a1>=a2 and b2>=b1:
     if a2==b1:
      a2+=1
      b1+=1
      p+=1
     else:
      a2+=1
elif a1>a2 and b2>b1 and b1<=a2:
   while a1>=a2 and b2>=b1:
     if a2==b1:
      a2+=1
      b1+=1
      p+=1
     else:
      b1+=1     
print(p)







          


