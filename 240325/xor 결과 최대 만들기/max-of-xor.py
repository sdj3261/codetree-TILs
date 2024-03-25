max_ret = 0
memo = {}  # XOR 연산 결과를 저장할 메모

def calculateXOR(nums):
    # 리스트를 튜플로 변환하여 딕셔너리의 키로 사용
    num_tuple = tuple(nums)
    if num_tuple in memo:
        return memo[num_tuple]

    result = nums[0]
    for num in nums[1:]:
        result ^= num
    
    memo[num_tuple] = result
    return result

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def combi(data, cnt, idx):
    global max_ret
    if cnt == m:
        max_ret = max(max_ret, calculateXOR(data))
        return 
    for i in range(idx, n):
        data.append(arr[i])
        combi(data, cnt+1, i+1)
        data.pop()

if m == 1:
    print(max(arr))
else:
    combi([], 0, 0)
    print(max_ret)