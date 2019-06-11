m=input()
l=[]
for i in m:
    if(i.isdigit())==True:
        l.append(i)
print(*l,sep="")
