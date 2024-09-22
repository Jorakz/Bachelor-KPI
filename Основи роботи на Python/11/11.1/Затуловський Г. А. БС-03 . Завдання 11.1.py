
def q():
 v = str(input('Добавить обновление в список? да/нет :'))
 if v == 'да':
    nov()
 else:
    print('Кінець роботи')


def nov():
    novi = []
    mesats = str(input( 'номер місяця випуску:'))
    novi.append(mesats)
    seh =str(input('номер цеху:'))
    novi.append(seh)
    code =str(input('код деталі:'))
    novi.append(code)
    kilk =str(input('кількість випущених деталей:'))
    novi.append(kilk)
    name =str(input('назва деталі:'))
    novi.append(name)
    output = open(r'details.txt', 'a', encoding='utf-8')
    output.write(' '.join(novi))
    output.close()
    q()
  
                  
details = open('details.txt', encoding='utf-8')
n =  len(details.readlines())
details.close()
details = open('details.txt', encoding='utf-8')
org1 = str(input('Виберіть цех: '))
org2 = str(input('Виберіть місяць роботи: '))
for x in range(n):
 k =details.readline()
 umov = k.split()
 while umov[0] == org2 and umov[1]== org1:
     print('назва деталі:',' '.join(umov[4:]),'\n',
           'код деталі:',umov[2],'\n',
           'кількість випущених деталей:',umov[3],'\n',
           'номер місяця випуску:',umov[0],'\n',
           'номер цеху:',umov[1],'\n',end='')
     print(' ')
     break
q()



    
 



