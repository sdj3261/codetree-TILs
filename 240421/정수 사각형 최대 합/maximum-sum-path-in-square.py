n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 초기값 세팅 
dp[0][0] = arr[0][0]

for i in range(1,n) :
    dp[i][0] = dp[i-1][0] + arr[i][0]
for j in range(1,n) :
    dp[0][j] = arr[0][j] + dp[0][j-1]

#점화식 세우기 dp[i][j] = max(위,왼쪽)
#출력 dp[n-1,n-1]

for i in range(1,n) :
    for j in range(1,n) :
        dp[i][j] = max(dp[i-1][j] + arr[i][j],dp[i][j-1] + arr[i][j]) 

print(dp[n-1][n-1])