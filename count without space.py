m = input()
count = 0
for i in m:
  if(i == " "):
    count = count + 1
counter = len(m) - count
print(counter)
