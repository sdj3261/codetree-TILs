import copy
import sys
sys.setrecursionlimit(10 ** 3)
selectBomb = []

def in_range(arr,y,x) :
    if 0<=y<=len(arr)-1 and 0<=x<=len(arr[0])-1 :
        return True
    return False

def dfs(arr,y,x,visited,num) :
    if num == 1 :
        dys = [-2,-1,1,2]
        dxs = [0,0,0,0]
    elif num == 2 :
        dys = [-1,0,1,0]
        dxs = [0,1,0,-1]
    else :
        dys = [-1,-1,1,1]
        dxs = [-1,1,-1,1]

    visited[y][x] = True

    for dy,dx in zip(dys,dxs) :
        ny = dy + y
        nx = dx + x
        if in_range(arr,ny,nx) == False or visited[ny][nx] == True:
            continue
        visited[ny][nx] = True

    
def combi(indexs,num) :
    if num == 0 :
        global selectBomb
        selectBomb.append(tuple(indexs))
        return 
    
    for i in range(1,4) :
        indexs.append(i)
        combi(indexs,num-1)
        indexs.pop()



n = int(input())
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))

bombCnt = 0
indexs = []

for i in range(n) : 
    for j in range(n) :
        if arr[i][j] == 1 :
            bombCnt +=1

combi(indexs,bombCnt)
max_ret = 0


for bomb in selectBomb :
    cnt = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    ret = 0

    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 and visited[i][j] == False:
                dfs(arr,i,j,visited,bomb[cnt])
                cnt+=1
    
    for i in range(n) :
        for j in range(n) :
            if visited[i][j] :
                ret+=1
    max_ret = max(ret,max_ret)
print(max_ret)