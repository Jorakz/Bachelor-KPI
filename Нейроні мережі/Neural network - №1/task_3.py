import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 11,1)
y = x**2
y2 = x**3
y3 = x+x
print("x=",x)
print("y1=",y)
print("y2=",y2)
print("y3=",y3)
plt.plot(x,y,label="X^2")
plt.plot(x,y2,label="X^3")
plt.plot(x,y3,label="X+X")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Graph")
plt.legend()
plt.show()
y_random = np.random.randint(100,size=len(x))
print("y_random = ",y_random)
plt.hist(y_random,bins=10,edgecolor ='black')
plt.xlabel("Values")
plt.ylabel("Frequnecy")
plt.title("Histogram")

plt.show()

