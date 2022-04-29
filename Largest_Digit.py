n=int(input())
max=0
l=[]
while(n>0):
    d=n%10
    l.append(d)
    n=n//10
for i in range(0,len(l)):
    if l[i]>max:
        max=l[i]
print(max)