s=input()
Sum=0
for i in range(0,len(s)):
    if s[i].isdigit():
        Sum=Sum+int(s[i])
print(Sum)