n=int(input())
num=list(map(int,input().split()))[:n]
c=0
for i in range(0,len(num)):
    c=0
    for j in range(0,len(num)):
        if num[j]<num[i] and j!=i:
            c+=1
    print(c,end=' ')