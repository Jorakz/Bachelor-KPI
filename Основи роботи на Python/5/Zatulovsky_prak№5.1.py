x = -2.4
xk = 1
dx = 0.2
b = 2.5
while x<=xk:
    y = 9*(x + 15*((x**3 + b**3)**(1/2)))
    print('x =', round(x,1),'|','y =', round(y,10))
    x = x + dx
   

    

