m,n = input().split()
x = int(m)
y = int(n)
for i in range(x+1,y):
  if(i % 2 != 0):
    print(i,end=" ")
