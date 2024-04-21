n = int(input())

# dp[1x2] + dp[2x1] + dp[2x2]


dp = [0] * 1002
dp[0] = 1
dp[1] = 1
dp[2] = 3
for i in range(3, n+1):
    dp[i] = (dp[i-1] + 2 * dp[i-2]) % 10007  # 점화식을 계산하면서 10007로 나누어줌
print(dp[n])