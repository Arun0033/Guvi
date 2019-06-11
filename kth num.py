num,n1=map(int,input().split())
m=list(map(int,input().split()))
for i in range(1,num+1):
    if i==n1:
        print(m[i-1])
