dp = [0] * (1001)
#i번쨰의 가짓수는 dp[i-2] + dp[i-3] 전에서 2번쨰로 올라온경우의수 더하기 3번쨰로 온 경우의수로 볼수있다.
#1. dp[0] = 1 ,dp[1] = 0 dp[2] = 1 dp[3] = 1
dp[0] = 1
dp[1] = 0
dp[2] = 1
dp[3] = 1

n = int(input())
for i in range(4,n+1) :
    dp[i] = dp[i-2] + dp[i-3] 
 
print(dp[n] % 10007)