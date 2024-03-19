import sys
sys.setrecursionlimit(10 ** 5)

def in_range(arr,y,x) :
    if 0<=y<=len(arr)-1 and 0<=x<=len(arr[0])-1 :
        return True
    return False

def dfs(arr,marble,t) :
    dys = [-1,1,0,0]
    dxs = [0,0,-1,1]
    mp = dict()
    next_marble_pos = []

    if t == 0 :
        print(len(marble))
        return 
    
    for my,mx in marble :
        cnt = -1
        marble_pos = None
        for dy,dx in zip(dys,dxs) :
            cnt+=1
            ny = my + dy
            nx = mx + dx
            
            if in_range(arr,ny,nx) == False:
                continue
            if marble_pos is None :
                marble_pos = arr[ny][nx]
                p = (ny,nx)
            if marble_pos < arr[ny][nx] :
                marble_pos = arr[ny][nx]
                p = (ny,nx)
        if cnt == 3 :
            if p in mp :
                mp[p] += 1
            else :
                mp[p] = 1

    for key,value in mp.items() :
        if value == 1 :
            next_marble_pos.append(key)
        
    dfs(arr,next_marble_pos,t-1)

        
n,m,t = map(int,input().split())
arr =  []
marble=[]

for i in range(n) :
    arr.append(list(map(int,input().split())))
for i in range(m) :
    y,x = map(int,input().split())
    marble.append((y-1,x-1))

dfs(arr,marble,t)