def is_isogram(s):
    for i in range(0,len(s)):
        for j in range(0,len(s)):
            if s[i]==s[j] and i!=j:
                return False
    return True
                
s=input()
if (is_isogram(s)==True):
    print('True')
else:
    print('False')