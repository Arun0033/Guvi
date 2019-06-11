r=int(input())
f=0
for i in range(2,r-1):
    if(r%i==0):
        f=1 
if(f==1):
    print("yes")
else:
    print("no")
