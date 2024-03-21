import sys
sys.setrecursionlimit(10 ** 4)
max_ret = 0
n = int(input())
dys = [-1,-1,0,1,1,1,0,-1]
dxs = [0,1,1,1,0,-1,-1,-1]
next_pos = list(zip(dys, dxs))
arr = []
direction = []
max_ret = 0
for i in range(n) :
    arr.append(list(map(int,input().split())))
for i in range(n) :
    direction.append(list(map(int,input().split())))

r,c = map(int,input().split())
r = r-1
c = c-1


def in_range(y,x) :
    if 0<=y<=len(arr)-1 and 0<=x<=len(arr)-1 :
        return True
    else :
        return False 

def dfs(arr,y,x,directionNum,ret,cnt) :
    global max_ret
    max_ret = max(ret,max_ret)
    dy,dx = next_pos[directionNum-1]

    if not in_range(y,x) :
        return
    if cnt == n :
        return
    for i in range(1,n) :
        ny = y + dy * i
        nx = x + dx * i 
        if not in_range(ny,nx) or arr[y][x] >= arr[ny][nx] :
            continue
        dfs(arr,ny,nx,direction[ny][nx],ret + 1,cnt+1)

dfs(arr,r,c,direction[r][c],0,1)
print(max_ret)