a=int(input())
n=int(input())
for i in range(a+1,n):
    var=0
    for j in range(2,i):
        if i%j==0 :
            var=var+1
    if var==0 :
        print(i)
