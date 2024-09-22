a=input('a = ')
b=input('b = ')
c=input('c = ')
s1=0
s2=0
s3=0
for x in a:
    s1+=int(x)
for x in b:
    s2+=int(x)
for x in c:
    s3+=int(x)
if(s1>s2 and s1>s3):
    print('Найбільша сума в числі:',a)
elif(s2>s3 and s2>s1):
    print('Найбільша сума в числі:',b)
else:
    print('Найбільша сума в числі:',c)    
