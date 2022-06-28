n=int(input())
arr=list(map(int,input().split()))[:n]
print("%.2f"%(sum(arr)/len(arr)))