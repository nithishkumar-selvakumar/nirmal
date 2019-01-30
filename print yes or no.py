n=int(input())
a,b=map(int,input().split())
c = 0
for i in range(a+1,b):
	if n == i:
		c = c + 1
if c == 1:
	print("yes")
else:
	print("no")
