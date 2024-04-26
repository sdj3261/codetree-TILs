n = int(input())
nums = list(map(int,input().split()))
dp = [0] * (n+1)

dp[0] = 1

# dp[i] : 마지막으로 고른 원소의 위치가 i인
# 부분 수열 중 최소 부분 수열의 길이
for i in range(1,n) : 
    for j in range(0,i) :
        if nums[i] < nums[j] :
            dp[i] = max(dp[i],dp[j]+1) 
print(max(dp))