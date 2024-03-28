from collections import deque
dys = [-1,0,1,0]
dxs = [0,1,0,-1]

n,k = map(int,input().split())
arr = []
start = []
for i in range(n) :
    arr.append(list(map(int,input().split())))

for i in range(k) :
    r,c = map(int,input().split())
    start.append((r-1,c-1))

visited = [[False for _ in range(n)] for _ in range(n)] 

q = deque()
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

            if arr[ny][nx] == 0 :
                visited[ny][nx]= True
                q.append((ny,nx))

for sy,sx in start :
    bfs(sy,sx)

ret = 0

for i in range(n) :
    for j in range(n) :
        if visited[i][j] :
            ret +=1
print(ret)