def calculateSquareB(arr,i,j) :
    sums = 0
    for n in range(i,i+2) :
        for m in range(j,j+2) :
            sums += arr[n][m]
    
    data = max(sums - arr[i][j], sums - arr[i+1][j], sums - arr[i][j+1], sums - arr[i+1][j+1])
    return data

def calculate3B(arr,i,j) :
    r = arr[i][j] + arr[i][j+1] + arr[i][j+2]
    c = arr[i][j] + arr[i+1][j] + arr[i+2][j]
    data = max(r,c)

    return data

n,m = map(int,input().split())
arr = []
ret = 0
for i in range(n) : 
    data = list(map(int,input().split()))
    arr.append(data)

for i in range(n-1) :
    for j in range(m-1) :
        ret = max(ret,calculateSquareB(arr,i,j))

for i in range(n-2) :
    for j in range(m-2) :
        ret = max(ret,calculate3B(arr,i,j))

print(ret)