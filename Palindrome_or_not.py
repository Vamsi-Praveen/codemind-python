s=input()
s=s.lower()
# print(s)
str = ""
for i in s:
    str = i + str
if str==s:
    print('True')
else:
    print('False')