n=int(input())
arr=[]
for i in range(1,n):
    if(n%i==0):
        arr.append(i)
Sum=sum(arr)
if(Sum==n):
    print("True")
else:
    print("False")
    