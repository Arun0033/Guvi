import math
ax=input().split()
ax=list(map(int,ax))
m=ax[0]*ax[1]
x=int(math.sqrt(m))
if x*x==m:
    print('yes')
else:
    print('no')
