n = int(input())
arr = []

for i in range(n) :
    arr.append(list(map(int,input().split())))


dys = [-1,0,1,0]
dxs = [0,1,0,-1]
max_ret = 0

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=n-1 :
        return True
    return False

def dfs(y,x,visited) :
    global max_ret
    visited[y][x] = True
    for dy,dx in zip(dys,dxs) :
        ny = dy + y
        nx = dx + x 

        if not in_range(ny,nx) or visited[ny][nx]:
            continue

        if arr[y][x] == arr[ny][nx] :
            dfs(ny,nx,visited)

tCount = 0 
bCnt = 0
blockBreakCnt = 0

for i in range(n) :
    for j in range(n) :
        tCount = 0
        visited = [[False for _ in range(n)] for _ in range(n)]
        #이미 방문했거나 폭탄 터진곳이면 패스
        if arr[i][j] == -1 or visited[i][j]:
            continue
        #탐색 시작     
        dfs(i,j,visited)

        blockCnt = 0

        for k in range(n) :
            for m in range(n) :
                if visited[k][m] :
                    blockCnt += 1
        max_ret = max(blockCnt,max_ret)

        if blockCnt >= 4 :
            for k in range(n) :
                for m in range(n) :
                    if visited[k][m] :
                        arr[k][m] = -1
            blockBreakCnt += 1
    




                                                                         
print(blockBreakCnt, max_ret)