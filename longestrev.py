n=input()
a=list(map(int, input().split()))
a.sort()
a.reverse()
for i in a:
	print(i,end="")
