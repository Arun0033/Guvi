z = input()
count1 = 0
count2 = 0
for i in z:
  if(i.isalnum()):
    count1 = count1 + 1
  if(i.isspace()):
    count2 = count2 + 1
counter = len(z) - count1 - count2
print(counter)
