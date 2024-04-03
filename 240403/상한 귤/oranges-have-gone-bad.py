from collections import deque
dys = [-1,0,1,0]
dxs = [0,1,0,-1]

n,k = map(int,input().split())
arr = []
visited = [[False for _ in range(n)] for _ in range(n)]
ret = [[0 for _ in range(n)] for _ in range(n)]
q = deque()

for i in range(n) :
    arr.append(list(map(int,input().split())))

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=n-1 :
        return True
    return False

def bfs(y,x) :
    visited[y][x] = True 
    q.append((y,x))

    while q :
        qy,qx = q.popleft()
        for dy,dx in zip(dys,dxs) :
            ny = qy + dy
            nx = qx + dx

            if not in_range(ny,nx) or visited[ny][nx] :
                continue

            if arr[ny][nx] == -1 :
                continue

            #귤 시간 체크
            if arr[ny][nx] == 1 :
                ret[ny][nx] = ret[qy][qx] + 1
                q.append((ny,nx))
                visited[ny][nx] = True


for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 0 :
            ret[i][j] = -1


for i in range(n) :
    for j in range(n) :
        if arr[i][j] == 2 :
            bfs(i,j)

for i in range(n) :
    for j in range(n) :
        print(ret[i][j], end = ' ')
    print()