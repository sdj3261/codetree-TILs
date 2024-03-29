from collections import deque

n = int(input())
r1,c1,r2,c2 = map(int,input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dys = [1,2,2,1,-1,-2,-2,-1]
dxs = [-2,-1,1,2,2,1,-1,-2]

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=n-1 :
        return True
    return False

q = deque()
 
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
            visited[ny][nx] = visited[qy][qx] + 1
            q.append((ny,nx))

bfs(r1-1,c1-1)
if visited[r2-1][c2-1] :
    print(visited[r2-1][c2-1]-1)
else :
    print(-1)