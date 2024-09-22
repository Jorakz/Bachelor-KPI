import random
names = []
adr = []
tel =[]
x1=[0,0,0,0,0,0,0]
d={}
y=10
for x in range (y):
    name = str(input('Введить призвище,имя,имя по батьков: '))
    names.append(name)
    adres = str(input('Введить адресу: '))
    adr.append(adres)
    for i in range(7):
        x1[i] = random.randint(0,9)
    tel.append(x1)
    x1=[0,0,0,0,0,0,0]
for u in range (y):
    items = dict([('Адреса',adr[u]),('Домашній телефон',tel[u])])
    d[names[u]]=items              
    u+=1
people = d
print('Cловник: ',d)
for i in range(y):
 if (people[names[i]]['Домашній телефон'])[-1] == 3:
    print('ПІБ :',names[i],'; Адреса: ',people[names[i]]['Адреса'],'; Номер домашнього телефону :',end='')
    n=0
    while 7>n:
        print(people[names[i]]['Домашній телефон'][n],end='')
        n+=1
    print(' ')

