def grow_one(x):
    o = 0
    for i in x:
        x[o] = 1 + i
        o = o+1



def check(a):
    if (a % 2 == 1):
        print("непарне")
    else:
        print("парне")


def for_(d):
    for i in d:
        print(i)


def while_(x):
    i = 0
    while (x[i] != 4):
        i = i + 1
    print(i)
a = 1 # - цілі числа
b = 0.1 # - дробові числа
c = "Hello World" # - рядки
d = [1,2,3,4,5] # - списки
f = {"good": 2, "bad":1} # - словники
print (a,"- цілі числа\n",b,"- дробові числа\n",c,"- рядки\n",d,"- списки\n",f,"- словники\n")
print("=============================")
a




check(a);
check(d[1])
print("=============================")
d = [1,2,3,4,5] # - списки
print(d,"- до функції")
grow_one(d)
print(d,"- після функції")
print("=============================")

d = [1, 2, 3, 4, 5]  # - списки

for_(d)
print('______')
while_(d)
