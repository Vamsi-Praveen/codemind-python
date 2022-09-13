n=int(input())
arr=list(map(int,input().split()))
o=[]
e=[]
for i in arr:
    if i%2==0:
        e.append(i)
    elif i%2!=0:
        o.append(i)
print(*(o+e))