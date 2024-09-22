def ch(k):
    s=[]
    prig = [ 'б', 'в', 'г', 'ґ', 'д'
                 , 'ж', 'з', 'к', 'л', 'м'
                 , 'н', 'п', 'р', 'с', 'т'
                 , 'ф', 'х', 'ц', 'ч','ш', 'щ']
    for x in range(len(k)):
        l = list(k[x])
        n1 = len(l)
        BIG =[]
        if x%2 == 0:
            for y in range(n1):
                if l[y] in prig:
                      l[y] = l[y].upper()
        BIG =(''.join(l))
        s.append(BIG)
    output = open(r'output.txt', 'w', encoding='utf-8')
    output.writelines(s)
    output.close()



input1 = open('input.txt',encoding='utf-8')
k = input1.readlines()
ch(k)
