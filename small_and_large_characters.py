s=input().split()
for i in s:
    l=[]
    for j in i:
        l.append(ord(j))
    print(chr(min(l)),chr(max(l)),end=' ')