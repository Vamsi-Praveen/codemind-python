n,m=map(int,input().split())
l=[]
Sum=0
for i in range(n):
    arr=list(map(int,input().split()))
    l.append(arr)
for i in l:
    for j in i:
        Sum+=j
print(Sum)