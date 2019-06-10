c = int(input())
b = []
for i in range(0,10):
  b.append(i)
  if(c == b[i]):
    print("yes")
    break
else:
  print("no")
