directions = ['R','D','L','U']

def checkRightWalls(arr,y,x,direction) :
    if direction == 'R' and arr[y+1][x] == '#':
        return True
    elif direction == 'D' and arr[y][x-1] == '#' :
        return True
    elif direction == 'L' and arr[y-1][x] == '#' :
        return True
    elif direction == 'U' and arr[y][x+1] == '#' :
        return True
    return False


def in_range(y,x) :
    if y >= 0 and y <n and x >=0 and x <n :
        return True
    else :
        return False

def directionToMove(direction) :
    if direction == 'R' :
        return (0,1)
    elif direction == 'D' :
        return (1,0)
    elif direction == 'L' :
        return (0,-1) 
    elif direction == 'U' :
        return (-1,0)

def dfs(arr, y, x, direction, visited, cnt):
    if not in_range(y, x) or arr[y][x] == '0':
        return cnt + 1  # 탐색 성공

    if visited[y][x][directions.index(direction)]:
        return -1  # 이미 방문했으므로 탐색 실패

    visited[y][x][directions.index(direction)] = True
    move = directionToMove(direction)

    ny = y + move[0]
    nx = x + move[1]

    if not in_range(ny, nx) or arr[ny][nx] == '0':
        return cnt + 1  # 탐색 성공

    if arr[ny][nx] == '#':
        # 현재 방향에서 오른쪽 벽을 확인 후 방향 전환
        return dfs(arr, y, x, directions[(directions.index(direction) - 1) % 4], visited, cnt)

    # 오른쪽 벽이 있다면 방향을 전환하고, 없다면 현재 방향을 유지
    next_direction = directions[(directions.index(direction) + 1) % 4] if checkRightWalls(arr, ny, nx, direction) else direction
    return dfs(arr, ny, nx, next_direction, visited, cnt + 1)


n = int(input())
r,c = map(int,input().split())
rightWall = False

visited = [[[False for _ in range(4)]for _ in range(n+2)] for _ in range(n+2)]
p = [r,c,directions[0],rightWall]

expanded_arr = [[0 for _ in range(n+2)] for _ in range(n+2)]
arr = []
for i in range(n) :
    arr.append(list(input()))

for i in range(1, n+1):
    for j in range(1, n+1):
        expanded_arr[i][j] = arr[i-1][j-1]

print(dfs(expanded_arr,r,c,'R',visited,1))