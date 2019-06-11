a,b = map(int,input().split())
z = input().split()
list = []
count = 0
for i in z:
  list.append(int(i))
for j in range(0,len(z)):
  if(list[j] == b):
    count = count + 1
print(count)
