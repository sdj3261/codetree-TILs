from collections import deque

dys = [-1,0,1,0]
dxs = [0,1,0,-1]
q = deque() 
n,m = map(int,input().split())
arr = []
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n) :
    arr.append(list(map(int,input().split())))

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=m-1 :
        return True
    return False

def bfs(y,x) :
    visited[y][x] = True
    q.append((y,x))

    while q :
        qy,qx = q.popleft()

        for dy,dx in zip(dys,dxs) :
            ny = dy + qy
            nx = dx + qx

            if not in_range(ny,nx) or visited[ny][nx] :
                continue

            if arr[ny][nx] == 1 :
                visited[ny][nx] = True
                q.append((ny,nx))

if arr[0][0] != 0 :
    bfs(0,0)

if visited[n-1][m-1] :
    print(1)
else :
    print(0)