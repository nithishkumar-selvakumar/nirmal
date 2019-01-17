a=int(input())
var=0;
for i in range(2,a):
    if a%i==0 :
        var=var+1
if var==0 :
    print("yes")
else :
    print("no")
