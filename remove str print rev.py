nm=int(input())
jj=input()
jj=list(jj)
l=[]
for i in jj:
    if(i!='a' and i!='e' and i!='o' and i!='i' and i!='u'):
        l.append(i)
m=l[::-1]
print(*m,sep="") 
