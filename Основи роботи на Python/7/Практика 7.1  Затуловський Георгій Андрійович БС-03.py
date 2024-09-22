import random 
m=int(input('введіть m=')) 
k=int(input('введіть k=')) 
while k<3 or k>10: 
    k=int(input('введіть k=')) 
i=0 
j=0 
while i<m: 
    j=0 
    while j<k and i<m: 
        print((random.randint(-77,127)), end=' ') 
        j+=1 
        i+=1 
    print()



     
