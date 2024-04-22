n = int(input())
arr = []
for i in range(n) : 
    arr.append(list(map(int,input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

dy = [0,1]
dx = [1,0]

ret = 10000001
move = []

def in_range(y,x) :
    if 0<=y<n and 0<=x<n :
        return True
    return False

def dfs(y,x) :
    global ret
    if y == n-1 and x == n-1 :
        maxData = max(move)
        ret = min(ret,maxData)
        return
    for ky,kx in zip(dy,dx) :
        ny = y + ky
        nx = x + kx

        if not in_range(ny,nx) :
            continue
        
        move.append(arr[ny][nx])
        dfs(ny,nx)
        move.pop()
dfs(0,0)
print(ret)