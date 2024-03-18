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

def dfs(arr,y,x,direction,visited,cnt) :
        # 범위를 벗어나는 경우나 종료 조건을 만족하는 경우
    if not in_range(y, x) or arr[y][x] == '0':
        return cnt + 1  # 탐색 성공

    # 이미 방문한 경우
    if visited[y][x][directions.index(direction)]:
        print(-1)
        return True  # 이 경우도 종료 조건이므로 True 반환

    visited[y][x][directions.index(direction)] = True
    move = directionToMove(direction)

    ny = y + move[0]
    nx = x + move[1]

    if not in_range(y, x) or ny == 0 or nx == 0:
        print(cnt + 1)
        return True  # 특정 조건을 만족하여 종료하는 경우 True 반환

    if arr[ny][nx] == '#' :
        dfs(arr,y,x,directions[directions.index(direction)-1],visited,cnt)

    if visited[ny][nx][directions.index(direction)] == False or arr[ny][nx] == '.' :
        if checkRightWalls(arr,ny,nx,direction) :
            dfs(arr,ny,nx,directions[directions.index(direction)+1],visited,cnt+1)
        else :
            dfs(arr,ny,nx,directions[directions.index(direction)],visited,cnt+1)


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

if dfs(expanded_arr,r,c,'R',visited,0) :
    pass