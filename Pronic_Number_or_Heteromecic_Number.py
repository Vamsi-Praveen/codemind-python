prno=int(input())
flg=0
for i in range(prno+1):
    if(i*(i+1)==prno):
        flg=1
        break
if flg==1:
    print('YES')
else:
    print('NO')