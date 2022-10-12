s1=input().lower()
s2=input().lower()
for i in s2.split():
    if i in s1.split():
        print(i,end=" ")