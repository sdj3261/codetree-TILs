from collections import deque
q = deque()
city = []
max_ret = 0
dys = [-1,0,1,0]
dxs = [0,1,0,-1]

def combi(idx, arr, cnt, k, visited):
    if cnt == k:
        city.append(list(arr))
        return
    if idx >= n * n:  # 모든 위치를 확인했다면 재귀 종료
        return

    i, j = divmod(idx, n)  # 일렬로 된 인덱스를 이용해 행과 열 계산

    # 현재 위치를 선택하지 않고 넘어가는 경우
    combi(idx + 1, arr, cnt, k, visited)
    
    # 현재 위치를 선택하는 경우
    if not visited[i][j]:
        visited[i][j] = True
        arr.append((i, j))
        combi(idx + 1, arr, cnt + 1, k, visited)
        visited[i][j] = False
        arr.pop()
    


n,k,u,d = map(int,input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))
m = []
visited = [[False for _ in range(n)] for _ in range(n)]

combi(0,m,0,k,visited)

def in_range(y,x) :
    if 0<=y<=n-1 and 0<=x<=n-1 :
        return True
    else :
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
            if u <= abs(arr[ny][nx] - arr[qy][qx]) <= d:
                visited[ny][nx] = True
                q.append((ny,nx))
        


for start in city :
    visited = [[False for _ in range(n)] for _ in range(n)]
    ret = 0
    for data in start :
        y = data[0]
        x = data[1]

        bfs(y,x)
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] :
                ret += 1
    max_ret = max(max_ret,ret)
print(max_ret)