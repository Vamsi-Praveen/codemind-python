n=int(input())
l=[]
while n!=0:
    d=n%10
    l.append(d)
    n=n//10
print(max(l))