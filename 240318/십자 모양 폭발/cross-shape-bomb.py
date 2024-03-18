def AfterGravity(arr) :
    for i in range(len(arr)) :
        for j in range(len(arr[i])) :
            if arr[i][j] == -1 :
                arr[i][j] = 0
                cnt = 0
                while i-cnt >= 1 :
                    arr[i-cnt][j] = arr[i-cnt-1][j]
                    arr[i-cnt-1][j] = 0
                    cnt+=1
    
            

def AfterbumbArr(arr, size, bumb) :
    arr[bumb[0]][bumb[1]] = -1
    for i in range(1,size) :
        if bumb[0]-i >= 0 :
            arr[bumb[0]-i][bumb[1]] = -1
        if bumb[0]+i < len(arr):
            arr[bumb[0]+i][bumb[1]] = -1
        if bumb[1]-i >= 0 :
            arr[bumb[0]][bumb[1]-i] = -1
        if bumb[1]+i < len(arr[0]) :
            arr[bumb[0]][bumb[1]+i] = -1



n = int(input())
arr = []

for i in range(n) :
    arr.append(list(map(int,input().split())))

bumb = list(map(int,input().split()))

bumb[0] = bumb[0] - 1
bumb[1] = bumb[1] - 1

size = arr[bumb[0]][bumb[1]]

AfterbumbArr(arr,size,bumb)
AfterGravity(arr)

for i in range(n) :
    print(" ".join(map(str,arr[i])))