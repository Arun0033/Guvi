import math
d,e=map(int,input().split())
m=math.gcd(d,e)
print((d*e)//m)
