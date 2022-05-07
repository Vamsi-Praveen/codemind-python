n=int(input())
arr=list(map(int,input().split()))
l=[]
for i in range(n):
    c=0
    f=0
    if(arr[i]<0):
        arr[i]=-(arr[i])
        f=1
    temp=arr[i]
    if(arr[i]==0):
        c=1
    while(arr[i]>0):
        d=arr[i]%10
        arr[i]=arr[i]//10
        c+=1
    l.append(c)
    arr[i]=temp
    if(f==1):
        arr[i]=-(arr[i])
k=max(l)
for i in range(n):
    c=0
    f=0
    if(arr[i]<0):
        arr[i]=-(arr[i])
        f=1
    temp=arr[i]
    if(arr[i]==0):
        c=1
    while(arr[i]>0):
        d=arr[i]%10
        arr[i]=arr[i]//10
        c+=1
    if(f==1):
        temp=-(temp)
    if(c==k):
        print(temp,end=" ")