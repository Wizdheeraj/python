a=input("Enter the string")
d={}
for i in a:
    keys=d.keys()
    if i in keys:
        d[i]+=1
    else:
        d[i]=1
print(d)

#method 2
a=input("enetr the string")
d={}
for i in a:
    d[i]=a.count(i)
print(str(d).replace(',','\n'))
