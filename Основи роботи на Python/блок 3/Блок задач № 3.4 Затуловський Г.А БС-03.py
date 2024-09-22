n = input('Введить слово: ')
slow = {
    'кот':'cat',
    'собака':'dog',
    'помидор':'tomato',
    'яблоко':'apple',
    'лес':'forest',
    'железо':'iron',
    'друг':'friend',
    'чай':'tea',
    'огонь':'fire',
    'хлеб':'bread'
    }
abc = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
slow_pr=False
for i in abc :
    if n[1].lower()==i:  
        slow_pr=True
        break
if slow_pr == True:
    print(slow[n])
    
else:
    for key, value in slow.items():
      if n in value:
       print(key)
