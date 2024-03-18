def in_range(r,c) :
    if r >= 0 and r<len(arr) and c >= 0 and c<len(arr[0]) :
        return True
    return False

def simulate(arr,r,c,visited) :
    visited[r][c] = True
    dys = [1,-1,0,0]
    dxs = [0,0,-1,1]

    for dy,dx in zip(dys,dxs) :
        ny = dy + r
        nx = dx + c

        if in_range(ny,nx) == False or visited[ny][nx] == True or arr[ny][nx] <= arr[r][c] :
            continue
        if visited[ny][nx] == False and in_range(ny,nx) and arr[ny][nx] > arr[r][c] :
            print(arr[ny][nx], end = ' ')
            simulate(arr,ny,nx,visited)
            break
n,r,c = map(int,(input().split()))
arr = []
for _ in range(n) :
    arr.append(list(map(int,input().split())))

r = r-1
c = c-1 

visited = [[False for _ in range(n)] for _ in range(n)]

print(arr[r][c], end=' ')
simulate(arr,r,c,visited)