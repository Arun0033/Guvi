n = int(input())
a = input().split()
s = []
for i in a:
  s.append(int(i))
c = sum(s) // n
print(c)
