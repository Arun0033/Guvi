ax=input()
z=ax.split('/')
x=ax.split('%')
for i in ax:
    if(i=='/'):
        print(int(z[0])//int(z[1]))
    elif(i=='%'):
        print(int(x[0]) % int(x[1]))
