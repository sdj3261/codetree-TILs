ret = []
n = int(input())

def dfs(arr,n,visited,cnt) :
    global ret
    if cnt == n :
        for i in arr :
            ret.append(i)
        return
    for i in range(3,0,-1) :
        if not visited[i] :
            arr.append(i)
            visited[i] = True
            dfs(arr,n,visited,cnt+1)
            arr.pop()
            visited[i] = False

arr = []
visited = [False] * (n+1)
dfs(arr,n,visited,0)

for i in range(len(ret)) :
    print(ret[i], end=' ')
    if i % n == n-1 :
        print()