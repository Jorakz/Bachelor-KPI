usa =  str(input())
a={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06',
   'July':'07','August':'08','September':'09','October':'10','November':'11','December':'12'}
usa = usa.replace('/',' ',2)
lst = usa.split()
if lst[1] in a:
    print(lst[0],'/', a[lst[1]],'/',lst[2])
else:
 lst[0],lst[1] = lst[1],lst[0]
 print(lst[0],'/',lst[1],'/',lst[2])
usa = usa.replace(' ','',2) 
