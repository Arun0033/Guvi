m=input()
m=list(m)
m[::2],q[1::2]=m[1::2],q[::2]
print(*m,sep="")
