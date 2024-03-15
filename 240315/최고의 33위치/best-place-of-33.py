def CalculateCoin(arr,a,b) :
    ret = 0
    
    for i in range(a,a+3) :
        for j in range(b,b+3) :
            if arr[i][j] == 1 :
                ret+=1
    return ret

n = int(input())
result = 0
arr = []

for i in range(n) :
    a = list(map(int,input().split()))
    arr.append(a)

for i in range(n-2) :
    for j in range(n-2) :
        result = max(CalculateCoin(arr,i,j),result)
print(result)