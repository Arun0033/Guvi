m=input()
m=m.split()
c=int(m[0])
d=int(m[1])
i=1
while(i<=c and i<=d):
    if(c%i==0 and d%i==0):
        gcd=i
    i=i+1
print(gcd)
