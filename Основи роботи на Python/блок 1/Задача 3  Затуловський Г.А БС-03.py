c1= int(input('Количество учеников в первом классе '))
while c1<=0:
     c1 = int(input('Количество учеников в первом классе '))
c2 = int(input('Количество учеников  во втором классе '))
while c2<=0:
     c2 = int(input('Количество учеников во втором классе '))
c3 = int(input('Количество учеников  во третьем классе '))
while c3<=0:
     c3 = int(input('Количество учеников в третьем классе '))
c=(c1+c2+c3)//2 +(c1+c2+c3)%2
print('Количество парт которые нужно купить для трех классов равняется ',c)
