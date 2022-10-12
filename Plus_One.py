n=int(input())
arr=list(map(int,input().split()))
x=""
for i in arr:
    i=str(i)
    x+=i
x=str(int(x)+1)
print(*list(x))