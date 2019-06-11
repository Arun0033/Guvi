m=input()
l=[]
m=list(map(int,m))
for i in m:
     if(i%2!=0):
         l.append(i)
print(*l,sep=" ")
