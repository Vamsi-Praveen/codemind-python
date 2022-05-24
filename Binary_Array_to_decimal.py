n=int(input())
arr=list(map(int,input().split()))[:n]
binary=''.join([str(elem) for elem in arr])
print(int(binary,2))