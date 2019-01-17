m=int(input())
n=int(input())
for i in range(m+1,n) :
    ans=0
    check_var=i
    b=len(str(i))
    while i>=1 :
      temp_digit=i%10
      temp_var=temp_digit**b
      ans=ans+temp_var
      i=int(i/10)
    if ans==check_var :
      print(check_var)
