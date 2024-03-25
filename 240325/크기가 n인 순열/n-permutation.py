def dfs(arr,visited,cnt,n) :
    if cnt == n :
        print(*arr)
        return
    for i in range(1,n+1) :
        if not visited[i] :
            arr.append(i)
            visited[i] = True
            dfs(arr,visited,cnt+1,n)
            arr.pop()
            visited[i] = False
n = int(input())
visited = [False] * (n+1)
arr = []
dfs(arr,visited,0,n)