import copy
max_ret = 0

def calculateXOR(nums) :
    #xor 연산시작
    nums[1] = nums[1] ^ nums[0]

    if len(nums) <= 2 :
        return nums[1]

    for i in range(2,len(nums)) :
        nums[i] ^= nums[i-1]
        
    return nums[-1]

n,m = map(int,input().split())

arr = list(map(int,input().split()))

def combi(data,cnt,idx) :
    global max_ret
    if cnt == m :
        max_ret = max(max_ret, calculateXOR(data))
        return 
    for i in range(idx,n) :
        data.append(arr[i])
        combi(data,cnt+1,idx+1)
        data.pop()

k = []

if m== 1 :
    print(max(arr))
else : 
    combi(k,0,0)
    print(max_ret)