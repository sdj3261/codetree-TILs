max_ret = 0
n = int(input())
arr = []
row_visited = [False for _ in range(n+1)]
col_visited = [False for _ in range(n+1)]

for i in range(n) :
    arr.append(list(map(int,input().split())))


def dfs(k,n,row) :
    global max_ret
    if row == n :
        sums = 0
        for y,x in k :
            sums += arr[y][x]
        max_ret = max(max_ret,sums)
        return
        
    for i in range(n) :
        if not col_visited[i] :
            k.append((row,i))
            col_visited[i] = True
            dfs(k,n,row+1)
            k.pop()
            col_visited[i] = False

k = []
dfs(k,n,0)
print(max_ret)