a=int(input())
sum=0
while a>0:
	t=a%10
	sum=sum+t
	a=a//10
print(sum)
