s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
c=0
for i in s1.split():
    if i in s2.split():
        c+=1
print(c)