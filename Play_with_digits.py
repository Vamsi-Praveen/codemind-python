def split_dig(n):
    s=0
    n=str(n)
    for i in n:
        s+=int(i)
    return s
n=int(input())
arr=list(map(int,input().split()))
Sum=0
l=[]
for i in range(0,len(arr)):
    Sum+=split_dig(arr[i])
print(Sum)