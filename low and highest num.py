n = int(input())
a = input().split()
s = []
for i in a:
  s.append(int(i))
print(min(s),end = " ")
print(max(s))
