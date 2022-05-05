n=int(input())
arr=list(map(int,input().split()))[:n]
a=[]
for i in arr:
    if arr.count(i)==i and i not in a:
        a.append(i)
if a==[]:
    print(-1)
else:
    print("%.2f"%(sum(a)/len(a)))