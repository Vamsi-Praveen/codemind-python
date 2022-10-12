n=input().lower().split()
n="".join(n)
c=0
for i in n:
    if(n.count(i)<=1):
        c+=1
print(c)