import sys
# 재귀 호출의 최대 깊이를 10000으로 설정
sys.setrecursionlimit(10000)
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
    if y >= 1 and y <=n+1 and x >=1 and x <=n+1 :
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
    if not in_range(y, x) or arr[y][x] == 0:
        return cnt

    direction_index = directions.index(direction)
    if visited[y][x][direction_index]:
        return -1  # 이미 방문했으므로 탐색 실패

    visited[y][x][direction_index] = True
    move = directionToMove(direction)

    ny = y + move[0]
    nx = x + move[1]

    if not in_range(ny, nx) or arr[ny][nx] == 0:
        return cnt + 1

    if arr[ny][nx] == '#':
        # 현재 방향에서 오른쪽 벽을 확인 후 왼쪽 90도로 방향 전환, 순환적으로 처리
        new_direction_index = (direction_index - 1) % 4
        return dfs(arr, y, x, directions[new_direction_index], visited, cnt)
    
    # 한 칸 이동했을 때 오른쪽 벽이 있다면 해당 방향으로 이동, 없다면 다음 방향으로
    if checkRightWalls(arr, ny, nx, direction):
        next_direction = direction
    else:
        new_direction_index = (direction_index + 1) % 4
        next_direction = directions[new_direction_index]
    return dfs(arr, ny, nx, next_direction, visited, cnt + 1)


n = int(input())
r,c = map(int,input().split())
rightWall = False

visited = [[[False for _ in range(4)] for _ in range(n+2)] for _ in range(n+2)]
p = [r,c,directions[0],rightWall]

expanded_arr = [[0 for _ in range(n+2)] for _ in range(n+2)]
arr = []
for i in range(n) :
    arr.append(list(input()))

for i in range(1, n+1):
    for j in range(1, n+1):
        expanded_arr[i][j] = arr[i-1][j-1]

print(dfs(expanded_arr,r,c,'R',visited,0))