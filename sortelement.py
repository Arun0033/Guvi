n = int(input())
a = input().split()
b = []
for i in range(0,n):
  b.append(int(a[i]))
  m = sorted(b)
for j in m:
  print(j,end=" ")
