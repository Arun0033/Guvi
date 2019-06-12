m=input()
m=list(m)
m[::2],m[1::2]=m[1::2],m[::2]
print(*m,sep="")
