n=int(input())
arr=list(map(int,input().split()))
Sum=Sum1=0
for i in range(0,n//2):
    Sum+=arr[i]
for j in range((n//2),n):
    Sum1+=arr[j]
print(abs(Sum-Sum1))