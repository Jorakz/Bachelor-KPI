Numb = int(input())
n1 = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
n2 = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
n3 = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
n4 = ["","M","MM","MMM","MMMM"]
ones = n1[Numb // 1 % 10]
ten = n2[Numb // 10 % 10]
hundr = n3[Numb // 100 % 10]
thous = n4[Numb // 1000]
print(thous+ hundr + ten + ones)
