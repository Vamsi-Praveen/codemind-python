n,m=map(int, input().split())
arr=[]
temp=n
c=0
s=0
r=0
while(n>0):
    d=n%10
    arr.append(d)
    n=n//10
    c+=1
n=temp
for i in range(0,m):
    s=(s*10)+arr[i]
for j in range(len(arr)-1,len(arr)-m-1,-1):
    r=(r*10)+arr[j]
n=0
while(s):
    n=(n*10)+(s%10)
    s=s//10
print(abs(n-r)) 