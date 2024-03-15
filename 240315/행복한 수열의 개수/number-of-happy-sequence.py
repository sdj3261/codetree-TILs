def count_seq(arr,m) :
    ret = 0
    max_ret = 0
    if len(arr) < 2 :
        return

    for i in range(len(arr)-1) :
        if ret == 0 and arr[i] == arr[i+1] :
            ret += 2
        elif arr[i] == arr[i+1] :
            ret += 1
        else :
            ret = 0
        max_ret = max(max_ret,ret)

    return max_ret >= m





n,m = map(int,input().split())
arr = []
if n == 1 :
    ret = 1
else :
    ret = 0

for i in range(n) :
    data = list(map(int,input().split()))
    arr.append(data) 

transposed_matrix = list(map(list, zip(*arr)))

for i in range(n) :
    data = arr[i]
    data2 = transposed_matrix[i]
    
    if m==1 :
        ret += n
    else :
        if count_seq(data,m) :
            ret += 1
        if count_seq(data2,m) :
            ret += 1
        
print(ret)