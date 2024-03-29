from collections import deque
n,m = map(int,input().split())
visited = [[0 for _ in range(m)] for _ in range(n)]
arr = []
q = deque()

dys = [-1,0,1,0]
dxs = [0,1,0,-1]
for i in range(n) :
    arr.append(list(map(int,input().split())))

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=m-1 :
        return True
    return False

def bfs(y,x) :
    visited[y][x] = 1
    q.append((y,x))

    while q :
        qy,qx = q.popleft()

        for dy,dx in zip(dys,dxs) :
            ny = dy + qy 
            nx = dx + qx

            if not in_range(ny,nx) or visited[ny][nx] :
                continue
            if arr[ny][nx] == 1 :
                visited[ny][nx] = visited[qy][qx] + 1
                q.append((ny,nx))
bfs(0,0)
if visited[n-1][m-1] :
    print(visited[n-1][m-1] - 1)
else :
    print(-1)