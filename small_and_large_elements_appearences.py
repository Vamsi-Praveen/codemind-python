s=input()
max=0
min=200
l=[]
for i in s:
    if i.isalnum():
        l.append(ord(i))
        if ord(i)>max:
            max=ord(i)
        if ord(i)<min:
            min=ord(i)
print(chr(min),l.count(min),chr(max),l.count(max))