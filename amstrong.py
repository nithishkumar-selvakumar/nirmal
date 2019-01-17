a=int(input())
check_var=a
b=len(str(a))
ans=0
while a>=1 :
    temp_digit=a%10
    temp_var=temp_digit**b
    ans=ans+temp_var
    a=int(a/10)
if ans==check_var :
    print("yes")
else :
    print("no")
