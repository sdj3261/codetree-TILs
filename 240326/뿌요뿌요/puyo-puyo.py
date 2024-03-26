n = int(input())
arr = []

for i in range(n) :
    arr.append(list(map(int,input().split())))


dys = [-1,0,1,0]
dxs = [0,1,0,-1]
blockCnt = 0
max_ret = 0

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=n-1 :
        return True
    return False

def dfs(y,x,block,visited) :
    global max_ret
    visited[y][x] = True
    for dy,dx in zip(dys,dxs) :
        ny = dy + y
        nx = dx + x 

        if not in_range(ny,nx) or visited[ny][nx]:
            continue

        if arr[y][x] == arr[ny][nx] :
            dfs(ny,nx,block+1,visited)
    max_ret = max(max_ret,block)

tCount = 0 
bCnt = 0
visited = [[False for _ in range(n)] for _ in range(n)]
boom = [[False for _ in range(n)] for _ in range(n)]

for i in range(n) :
    for j in range(n) :
        if boom[i][j] :
            continue
        visited = [[False for _ in range(n)] for _ in range(n)]
        dfs(i,j,0,visited)
        tCount = 0
        
        for k in range(n) :
            for m in range(n) :
                if visited[k][m] :
                    tCount += 1
                    max_ret = max(tCount,max_ret)
        if tCount >= 4 :
            boom = visited
            bCnt += 1

                                                                         
print(bCnt, max_ret)