def is_isogram(s):
    return (len(s)==len(set(s.lower())))
s=input()
if (is_isogram(s)==True):
    print('True')
else:
    print('False')