m=input().split()
x=int(m[0])
y=int(m[1])
for i in range(x+1,y):
  t=i
  sum=0
  while(t!=0):
    r=t%10
    sum=sum+(r*r*r)
    t=t//10
  if(sum==i):
    print(i)
  else:
    continue
