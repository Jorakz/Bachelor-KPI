import random


def MinesAround( FieldForMine, i, j):
    """Перевіряє кількість мін навколо точки з
       координатами i, j
    """
    FieldForMine = FieldForMine + [0]* (hight*(wight - hight))
    n = 0
    for k in range(-1,2):
        for l in range(-1,2):
            x = i+k
            y = j+l
            if x<0 or x >= wight or y <0 or y >= hight:
                continue
            if FieldForMine[x*hight+y] == '*':
                n +=1
            FieldForMine[x*hight+y] = n
    return n 
     
def createGame(FieldForMine,x,y):
    """ Создає ігрове поле: положення мін
        та рахунок кількості мін навколо комірки
        без міни
    """
    rand = random.Random()
    n = mine
    m=0
    blockMINE=[]
    for k in range(-1,2):
        for l in range(-1,2):
            x1 = x+k
            y1 = y+l            
            blockMINE.append(x1*hight+y1)
    while n>0:
        i = rand.randrange(wight)
        j = rand.randrange(wight)
        if  i*hight+j in blockMINE:
            continue
        if FieldForMine[i*hight+j] != 0:
            continue        
        FieldForMine[i*hight+j] = '*'
        n -=1    
    for i in range(wight):
        for j in range(wight):
            if FieldForMine[i*hight+j] == 0:
                FieldForMine[i*hight+j] = MinesAround( FieldForMine, i, j)    
    del FieldForMine[(wight*hight):]
    
                
    
def showField(FieldForMine,FieldForPlayer):
    """ Функція показує стан поля гри"""
    for i in range(wight):
        for j in range(hight):            
            print(str(FieldForPlayer[i*hight+j]).rjust(3),end="")
        print()


def PlayerChoice():
   """ Функція для вибору гравцем координат
       закритой комірки ігрового поля
   """
   flLoopInput = True
   while flLoopInput:
       try:
        x,y = input("Введіть координату через пробіл: ").split()
       except ValueError:
        x,y = input("Введіть координату через пробіл: ").split()       
       if not x.isdigit() or not y.isdigit():
           print("Координати введені невірно")
           continue
       x= int(x)-1
       y= int(y)-1
       if x < 0 or x >= wight or y<0 or y >= hight:
           print("Координати виходять за межу поля")
           continue       
       flLoopInput = False
   return x,y

       
def Finish(FieldForMine,FieldForPlayer):
    """Перевірка стану гри:
       Гра продовжуеться, перемога, поразка
    """
    for i in range(wight*hight): 
        if str(FieldForPlayer[i]) != 'X' and str(FieldForMine[i]) == '*' and str(FieldForPlayer[i]) !='F' and str(FieldForPlayer[i]) != '?' :
            return -1
    for i in range(wight*hight): 
        if str(FieldForPlayer[i]) == 'X' and str(FieldForMine[i]) != '*':
            return 1
    return -2
    

def Score(FieldForMine,FieldForPlayer):
    """
       Функція рахує кількість балів за гру
       та записує результат у список всіх
       результатів
    """
    for i in range(wight):
        for j in range(hight):
            print(str(FieldForMine[i*hight+j]).rjust(3),end="")
        print()
    print('')
    score =0
    if Finish(FieldForMine,FieldForPlayer) != -1:
        score+= hight*wight*2
        print('Ви перемогли')
    for y in range(hight):
     for x in range(wight):
       if str(FieldForPlayer[x*hight + y]) != 'X':
        score+=1
       if Finish(FieldForMine,FieldForPlayer) == -1:
        if str(FieldForPlayer[x*hight + y]) == 'F' and FieldForMine[x*hight + y] == '*':
         score+=5
    if Finish(FieldForMine,FieldForPlayer) != -1:
        score+= FieldForMine.count('*') * 5
    if Finish(FieldForMine,FieldForPlayer) == -1:
        print('Ви програли')
    print('Счет за гру: ',score)
    print('')
    all_s=  open(r'top.txt','r',encoding ='utf-8')
    all_score = all_s.readlines()
    all_s.close()
    all_score.append( '\n' + str(score) + ' '+ str(name_player))
    Top =  open(r'top.txt','w',encoding ='utf-8')
    Top.writelines(all_score)
    Top.close()
    menu()
    
def check(FieldForPlayer,FieldForMine,i,j,check_activ):
     """ функція перевіряє, чи не виходять координати задані гравцем
        за границі поля та вміст певної комірки 0. якщо так
        функція відкриває цю комірку, записуючи у список перевіряних,
        та перевіряє вміст сосідніх комірок
     """
     check_list=[]
     if FieldForMine[i*hight+j] == 0 and [i,j] not in check_activ:
        check_activ.append([i,j])
        for k in range(-1,2):
          for l in range(-1,2):
            x = i+k
            y = j+l
            if x<0 or x >= wight or y <0 or y >= hight:
                continue
            FieldForPlayer[x*hight+y]=FieldForMine[x*hight+y]
            if FieldForMine[x*hight+y] == 0  and x*hight+y != i*hight+j :
                check_list.append([x,y])
                check(FieldForPlayer,FieldForMine,x,y,check_activ)
             

      
    
def start():
    """ Функція запуска гри: Просить задати перші координати та визиває функцію
        перевірки та заповнення поля мінами
    """
    FieldForPlayer = ['X']*hight*wight
    FieldForMine = [0]*wight*wight
    x=0
    y=0
    check_activ=[]
    showField(FieldForMine,FieldForPlayer)
    print('Координати комірок ігрового поля відповідають значенням індексів елементів матриці')
    x,y = PlayerChoice()
    createGame(FieldForMine,x,y)
    check(FieldForPlayer,FieldForMine,x,y,check_activ)
    FieldForPlayer[x*hight+y] = FieldForMine[x*hight+y]
    mine_left = mine
    print('Всього мін: ', mine)
    print('Мін залишилося: ', mine_left )
    start2(FieldForMine,FieldForPlayer,mine_left,check_activ)
    
def save(FieldForMine,FieldForPlayer,mine_left,check_activ):
    """
       Функція сохроняє ігровий процес, імя та пароль гравця
    """
    save_w = open(r'save_for_player.txt', 'w',encoding = 'utf-8')
    FP=''
    for a in range(len(FieldForPlayer)):
     FP += str(FieldForPlayer[a])
    save_w.writelines(FP)
    save_w.close()
    FM = []    
    save_x = open('save_mine.txt', 'w', encoding = 'utf-8')
    bits = bin(int.from_bytes(str(FieldForMine).encode('utf-8','surrogatepass'),'big'))[2:]
    FM1 = bits.zfill(8 * ((len(bits) + 7) // 8))
    save_x.writelines(FM1)
    save_x.close()
    save_q = open('login.txt','w')
    save_q.write((name_player+'\n'))
    save_q.write((password_player+'\n'))
    save_q.write((str(hight)+'\n'))
    save_q.write((str(wight)+'\n'))
    save_q.write((str(mine_left)+'\n'))
    save_q.write((str(mine)+'\n'))
    save_q.write((str(check_activ)))
    save_q.close()
    
def start2(FieldForMine,FieldForPlayer,mine_left,check_activ):
 """ Функція гри: відоброжає поле гри,
        ігрок відкириває закриту комірку
        результат перевіряється на виграшну ситуацію
        (всі комірки відкриті) або пораження
        (у відкритій комірці була міна)
 """
 while Finish(FieldForMine,FieldForPlayer) > 0:
       showField(FieldForMine,FieldForPlayer)
       print(' відкрити комірку - 1 \n поставити флаг - 2 \n прибрати флаг - 3 \n постивити ? - 4 \n прибрати ? - 5 \n зберегти гру - 6 \n вийти в меню - 7\n')
       q = input('Виберіть дію: ')
       while str(q).isdigit() == False:
           q = input('Виберіть дію: ')
       if int(q) == 1: 
         x,y = PlayerChoice()
         if FieldForPlayer[x*hight+y] != 'F' :
           check(FieldForPlayer,FieldForMine,x,y,check_activ)    
           FieldForPlayer[x*hight+y] = FieldForMine[x*hight+y]
       elif int(q) == 2 and mine_left > 0 :
           x,y = PlayerChoice()
           if FieldForPlayer[x*hight+y] != 'F' and FieldForPlayer[x*hight+y] == 'X' or FieldForPlayer[x*hight+y] == '?':
            FieldForPlayer[x*hight+y] = 'F'
            mine_left -= 1
       elif int(q) == 3 and mine_left < mine:
           x,y = PlayerChoice()
           if FieldForPlayer[x*hight+y] == 'F':
            FieldForPlayer[x*hight+y] = 'X'
            mine_left += 1
       elif int(q) == 4:
          x,y = PlayerChoice()
          if FieldForPlayer[x*hight+y] == 'X':
            FieldForPlayer[x*hight+y] = '?'
       elif int(q)  == 5:
          x,y = PlayerChoice()
          if FieldForPlayer[x*hight+y] == '?':
             FieldForPlayer[x*hight+y] = 'X'
       elif int(q) == 6:
           save(FieldForMine,FieldForPlayer,mine_left,check_activ)
       elif int(q) == 7:
           menu()
       print('Всього мін: ', mine)
       print('Мін залишилося: ', mine_left )
 Score(FieldForMine,FieldForPlayer)


       
def level():
 """
    Функція яка дає можливіть вибрати складність гри,
    пароль та логін
 """
 print('Виберіть складність:','Новачок - 1','Любитель - 2','Професіонал - 3', sep='\n')
 levels=(('Новачок',9,9,10),('Любитель',16,16,40),('Професіонал',30,16,90))
 c=int(input()) - 1
 while c<0 or c>2:
     print('Виберіть складність:','Новачок - 1','Любитель - 2','Професіонал - 3', sep='\n')
     c=int(input()) - 1
 global name_player
 global password_player
 name_player = str(input('Введіть імя грався: '))
 password_player = str(input('Введіть пароль: '))
 global hight
 global wight
 global mine
 hight= levels[c][2]
 wight= levels[c][1]
 mine= levels[c][3]


 
def download_last_game():
    """
       Функція загружає останню гру, після ведення імя та пароля гравця
    """
    log = open('login.txt','r')
    global name_player
    global password_player
    name_player = (log.readline()).rstrip()
    password_player = (log.readline()).rstrip()
    w = True
    w1 = 0
    while w == True:
       print ('Повернутися в меню - 1 ')
       name_check= input('Введіть імя грався: ')
       password_check = input('Введіть пароль: ')
       print(' ')
       if name_check == name_player and password_check == password_player:
           w = False
           w1 = 1
       elif name_check == '1' and password_check == '1':
           w = False
           w1 = -1
    if w1 == 1:
        global hight
        global wight
        global mine
        FieldForMine = []
        FieldForPlayer = []
        hight = int((log.readline()).rstrip())
        wight = int((log.readline()).rstrip())
        mine_left = int((log.readline()).rstrip())
        mine = int((log.readline()).rstrip())
        check_activ_str = log.readline()
        m = check_activ_str
        n = eval(check_activ_str)
        check_activ = n        
        log.close()
        play_field = open('save_for_player.txt', 'r')
        FP = play_field.readline()
        for fp in range (len(FP)):
            if FP[fp].isdigit():            
              FieldForPlayer.append( int(FP[fp]))
            else:
              FieldForPlayer.append( FP[fp])
        play_field.close()
        mine_field = open('save_mine.txt', 'r')
        bits1 = mine_field.readlines()
        bits =bits1[0]
        n = int(bits, 2)
        revert=list(n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0')
        for d1 in range(revert.count(',')):
            revert.remove(',')
        for d1 in range(revert.count(' ')):
            revert.remove(' ')
        for d1 in range(revert.count('[')):
            revert.remove('[')
            revert.remove(']')
        for d1 in range(revert.count("'")):
            revert.remove("'")
        for fm in range (len(revert)):
            if revert[fm].isdigit():
                FieldForMine.append(int(revert[fm]))
            else:
                FieldForMine.append(revert[fm])
        mine_field.close()
        print('Всього мін: ', mine)
        print('Мін залишилося: ', mine_left )
        start2(FieldForMine,FieldForPlayer,mine_left,check_activ)
    if w1 == -1:
        menu()

        
def menu():
 if __name__ == '__main__':
  print('Нова гра - 1','Продовжити гру - 2','Локальний рейтинг - 3','Глобальний рейтинг - 4', sep='\n')      
  choice = input()
  if str(choice).isdigit() == False:
    menu()
  elif int(choice) == 1:
    level()
    start()    
  elif int(choice) == 2:
     download_last_game()
  elif int(choice) == 3:
     local_top()
  elif int(choice) == 4:
     global_top()
  else:
    menu()

def local_top():
    """
       Функція показує статистику из 10 найкращих спроб певного грався
    """
    name = str(input('Введіть імя гравця: '))
    local = open(r'top.txt',encoding ='utf-8')
    n = len(local.readlines())
    local.close()
    local = open(r'top.txt',encoding ='utf-8')
    L=[]
    num = []
    for x in range(n):
       k =local.readline()
       l = k.split()
       if l[1] == name:
         L.append(l)
         num.append(l[0])
       num =[int(elt) for elt in num]
    for x in range(len(L)):
     L[x][0] = num[x]
    L.sort(key=lambda i: i[0], reverse =True)
    n=0
    print('\nЛокальний рейтинг гравця',name)
    for i in L:
        if n<10:
         print(i[1],'очки:',i[0])
         n+=1
    print('')
    local.close()
    menu()

 
def global_top():
    """
       Функція показує статистику из 10 найкращих спроб серед всіх гравців
    """
    local = open(r'top.txt',encoding ='utf-8')
    n = len(local.readlines())
    local.close()
    local = open(r'top.txt',encoding ='utf-8')
    L=[]
    num = []
    for x in range(n):
       k =local.readline()
       l = k.split()
       L.append(l)
       num.append(l[0])
       num =[int(elt) for elt in num]
    for x in range(len(L)):
     L[x][0] = num[x]
    L.sort(key=lambda i: i[0], reverse =True)
    n=0
    print('\nГлобальний рейтинг всіх гравців')
    for i in L:
        if n<10:
         print(i[1],'очки:',i[0])
         n+=1
    print('')
    local.close()
    menu()
menu()
