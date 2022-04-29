s=input()
arr=[]
for i in range(0,len(s)):
    if s[i].isdigit():
        arr.append(int(s[i]))
print(sum(arr))