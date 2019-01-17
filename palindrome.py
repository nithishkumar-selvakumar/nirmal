original_val=int(input())
b_ip=str(original_val)
n=b_ip[::-1]
reverse_val=int(n)
if original_val==reverse_val :
    print("yes")
else :
    print("no")
