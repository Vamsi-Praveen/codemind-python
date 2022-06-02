n=input()
w=n.split()
for i in range(0,len(w)):
    if i%2==0:
        print(w[i][::-1],end=' ')
    else:
        print(w[i],end=" ")