import sys
sys.recursionlimit(10 ** 3)
def checkSeqThree(arr) :
    i = 0
    cnt = 1
    while i < len(arr)-1 :
        if arr[i] == arr[i+1] :
            cnt +=1
            if cnt == 3 :
                return True
        else :
            cnt = 1
        i+=1   
    return False

def conditionCombi(arr,n,k) :
    if n == 0 and not checkSeqThree(arr) :
        print(*arr)
        return
    for i in range(1,k+1) :
        arr.append(i)
        conditionCombi(arr,n-1,k)
        arr.pop()

k,n = map(int,input().split())
arr = []
conditionCombi(arr,n,k)