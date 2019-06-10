m = int(input())
a = 0
b = 1
for i in range(0,m):
  print(b,end = " ")
  c = a + b
  a = b
  b = c
