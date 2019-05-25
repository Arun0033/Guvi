p=input()
p=p.split()
N=int(p[0])
K=int(p[1])
m=input()
m=m.split()
sum=0
for i in range(K):
  sum=sum+int(m[i])
print(sum)
