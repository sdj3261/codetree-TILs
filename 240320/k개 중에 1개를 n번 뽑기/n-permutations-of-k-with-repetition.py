def dfs(k,n,arr) :
    if n == 0 :
        print(*arr)
        return
    for i in range(1,k+1) :
        arr.append(i)
        dfs(k,n-1,arr)
        arr.pop() 
k,n = map(int,input().split())
arr = []
dfs(k,n, arr)