max_ret = 0
n = int(input())
arr = []
row_visited = [False for _ in range(n+1)]
col_visited = [False for _ in range(n+1)]

for i in range(n) :
    arr.append(list(map(int,input().split())))


def dfs(k,cnt,n) :
    global max_ret
    sums = 0
    for y,x in k : 
        sums += arr[y][x]

    if cnt == n :
        max_ret = max(max_ret,sums)
        return
    for i in range(n) :
        for j in range(n) :
            if not row_visited[i] and not col_visited[j] :
                k.append((i,j))
                row_visited[i] = True
                col_visited[j] = True
                dfs(k,cnt+1,n)
                k.pop()
                row_visited[i] = False
                col_visited[j] = False

k = []
dfs(k,0,n)
print(max_ret)