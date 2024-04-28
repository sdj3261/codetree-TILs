#dp[i] = 동전의합이 i원일떄 가장 효율적인 동전의 개수
n,m = map(int,input().split())
coin = list(map(int,input().split()))
dp = [100000] * 10001

for i in range(1,m+1) :
    for j in range(n) :
        if i >= coin[j] :
            if dp[i-coin[j]] == 100000 :
                continue
            dp[i] = min(dp[i],dp[i-coin[j]] + 1)
    if dp[i] == 100000 :
        dp[i] = -1
    
print(dp[m])