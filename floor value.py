import math
nn=input()

nn=nn.split()
pp=int(nn[0])
tt=int(nn[1])
rr=int(nn[2])
ss=pp*tt*rr//100
print(math.floor(ss))
