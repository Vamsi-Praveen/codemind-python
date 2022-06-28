n=int(input())
arr=[]
v=0
while n!=0:
    d=n%10
    arr.append(d)
    n=n//10
for i in arr:
    for j in arr:
        if i==j:
            v+=1
if v==len(arr):
    print("Unique Number")
else:
    print("Not Unique Number")