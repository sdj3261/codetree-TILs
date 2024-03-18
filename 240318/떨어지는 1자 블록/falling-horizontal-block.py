def in_range(y,x) :
    if y>=0 and y < len(arr) and x >= 0 and x < len(arr[0]) :
        return True
    return False

def dfs(arr,y,x) :
    ny = y+1
    nx = x

    if in_range(ny,nx) == False or arr[ny][nx] == 1 :
        visited[ny-1][nx] = 1
        return
    dfs(arr,ny,nx)

n,m,k = map(int,input().split())
visited = [[0 for _ in range(n)] for _ in range(n)]
arr = []
for _ in range(n) :
    arr.append(list(map(int,input().split())))

#k-1, k+m-1 까지 dfs 아래로 쭉 체크해서 minHeight 계산
for i in range(k-1,k+m-1) :
    dfs(arr,0,i)

minHeight = n-1

#minHeight 체크 후 k-1부터 k+m-1 까지 모두1로 치환
for i in range(n) : 
    for j in range(n) :
        if visited[i][j] == 1 :
            minHeight = min(minHeight, i)
            break

for i in range(k-1,k+m-1) :
    arr[minHeight][i] = 1  

for i in range(n) :
    print(" ".join(map(str,arr[i])))