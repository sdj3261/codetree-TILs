n,m = map(int,input().split())
arr = []
visited = [[False for _ in range(n)] for _ in range(m)]

ret = -1

for i in range(n) : 
    arr.append(list(map(int,input().split())))

# dfs하고 양수일때만 arr 넘기기 직사각형이면 max 크기재기
#직사각형 찾기
dy = [1,0,-1,0]
dx = [0,1,0,-1]


def is_rectangle(visited):
    min_x = min_y = 1004
    max_x = max_y = -1004
    true_positions = []
    isRect = True

    # `True` 값의 위치를 찾고, 최소/최대 x, y 좌표를 계산
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j]:
                true_positions.append((i, j))
                min_x = min(min_x, i)
                max_x = max(max_x, i)
                min_y = min(min_y, j)
                max_y = max(max_y, j)

    # 찾아진 모든 `True` 값이 직사각형을 형성하는지 확인
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not visited[x][y]:
                isRect = False
    if isRect : 
        r = max_x - min_x + 1
        c = max_y - min_y + 1
        return r*c

    return -1





def in_range(y,x) :
    if 0<=y<n and 0<=x<m :
        return True
    return False
def dfs(y,x) :
    global ret
    visited[y][x] = True

    ret = max(ret,is_rectangle(visited))
    
    for ky,kx in zip(dy,dx) :
        ny = ky + y 
        nx = kx + x

        if not in_range(ny,nx) or visited[ky][kx] :
            continue
        if arr[ky][kx] > 0 :
            dfs(ny,nx)

for i in range(n) : 
    for j in range(m) :
        if arr[i][j] > 0 :
            dfs(i,j)
print(ret)