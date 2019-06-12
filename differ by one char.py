q=input()
q=q.split()
w=list(q[0])
w2=list(q[1])
m=0
for i in range(0,len(w)):
    if(w[i]==w2[i]):
        m=m+1
if(m==len(w)-1):
    print("yes")
else:
    print("no") 
