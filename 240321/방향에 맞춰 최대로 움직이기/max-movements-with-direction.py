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

def calculatePos(arr,y,x,directionNum) :
    result = []
    dy,dx = next_pos[directionNum-1]

    for i in range(1,n) :
        ny = y + dy * i
        nx = x + dx * i 
        if not in_range(ny,nx) or arr[y][x] >= arr[ny][nx] :
            continue
        result.append((ny,nx))
    return result

def dfs(arr,y,x,directionNum,ret) :
    #1턴마다 모든 조합 경우의 수 max_Ret 구하기
    global max_ret
    max_ret = max(max_ret, ret) 
    pos_data = calculatePos(arr,y,x,directionNum)
    if len(pos_data) == 0 :
        return

    for posy,posx in pos_data :
        dfs(arr,posy,posx,direction[posy][posx],ret+1)   

dfs(arr,r,c,direction[r][c],0)
print(max_ret)