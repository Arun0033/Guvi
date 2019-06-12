n,n1=map(int,input().split())
a=list(map(int,input().split()))
m=[]
for i in a:
    if i%2!=0:
        m.append(i)
for i in range(1,len(m)+1):
    if i==n1:
        print(m[i-1])
