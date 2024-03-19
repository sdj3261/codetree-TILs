def in_range(arr,y,x) :
    if 0<=y<=len(arr)-1 and 0<=x<=len(arr[0])-1 :
        return True
    return False
def dfs(arr,y,x) :
    dys = [-1,-1,-1,0,1,1,1,0,]
    dxs = [-1,0,1,1,1,0,-1,-1]
    max_value = 0
    max_value_pos = (0,0)

    for dy,dx in zip(dys,dxs) :
        ny = dy + y
        nx = dx + x
        if in_range(arr,ny,nx) == False:
            continue
        if max_value < arr[ny][nx] :
            max_value = arr[ny][nx]
            max_value_pos = (ny,nx)

    temp = arr[y][x]
    arr[y][x] = arr[max_value_pos[0]][max_value_pos[1]]
    arr[max_value_pos[0]][max_value_pos[1]] = temp

n,m = map(int,input().split())
arr = []
for i in range(n) :
    arr.append(list(map(int,input().split())))

flag = 0

for _ in range(m) :
    for k in range(1,n**2 + 1) :
        flag = 0
        for i in range(n) :
            for j in range(n) :
                if arr[i][j] == k and flag == 0:
                    flag = 1
                    dfs(arr,i,j)
    
        if flag == 1 :
            flag = 0
            continue
for i in range(n) :
    print(" ".join(map(str,arr[i])))