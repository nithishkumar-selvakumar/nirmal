a=int(input())
n=int(input())
val=a
for i in range(a+1,n):
    val=val+1
    if val%2!=0 :
        print(val)
