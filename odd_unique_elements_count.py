n=int(input())
arr=list(map(int,input().split()))[:n]
c=0
l=[]
for i in arr:
    if i not in l:
        l.append(i)
for i in l:
    if i%2!=0:
        c+=1
print(c)
        