import array
n_ip=int(input())
k=int(input())
sum=0
arr = array.array('i', [])
for j in range(0,n_ip):
    a_ip=int(input())
    arr.append(a_ip);
for m in range(0,k):
    sum=int(sum+arr[m])
print(sum)
