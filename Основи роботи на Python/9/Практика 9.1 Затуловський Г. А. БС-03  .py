strokpr = input('Введіть строку:')
s = list(strokpr)
for x in range(len(s)):
 simv = ['.','-', ',', '"', '(', '[',':',';']
 if s[x] in simv:
   strokpr = strokpr.replace(s[x],' ')
strok = str(strokpr)
elem = strokpr.split()
lis = strok.split()
print('Числа:',end=' ')
for word in elem:
    if word.isnumeric():
        print(int(word),end='; ')  # частина кода, що шукае числа в рядку
print('')

n=0
print('Слова написанні на латині: ',end=' ')
while len(lis) > n:
    elemword = list(lis[n])
    abc ={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
    c = 0
    for x in range (len(elemword)):
        if elemword[x] in abc:
          c+=1
    if c == len(elemword):
        print(lis[n],end ='; ') # частина кода, який шукае слова на латині
    n+=1
print('')

n =0
lis = strok.split()
print('Видалення кожного другого слова з рядка: ',end='')
while len(lis) >= n:
    if n % 2 == 0 and n!= 0:
        lis[n-1] = ''
    n+=1                       # Частина кода, яка видаляе кожне друге слово
while lis.count('') != 0:
    lis.remove('')
n=0
while len(lis) > n:
    print(lis[n],end = ' ')
    n+=1

