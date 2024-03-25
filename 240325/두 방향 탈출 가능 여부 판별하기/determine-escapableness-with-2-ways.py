n,m = map(int,input().split())
visited = [[False for _ in range(m)] for _ in range(n)]
arr = []
dys = [1,0]
dxs = [0,1]

for i in range(n) :
    arr.append(list(map(int,input().split())))

def in_range(y,x) :
    if 0<=y<=len(arr)-1 and 0<=x<=len(arr[0])-1 :
        return True
    return False

def dfs(y,x,visited) :
    visited[y][x] = True
    for dy,dx in zip(dys,dxs) :
        ny = y + dy
        nx = x + dx

        if not in_range(ny,nx) or visited[ny][nx] == True or arr[ny][nx] == 0 :
            continue
        dfs(ny,nx,visited)

dfs(0,0,visited)

if visited[n-1][m-1] == True :
    print(1)
else :
    print(0)