n = int(input())
arr = []
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n) :
    arr.append(list(map(int,input().split())))

start = arr[0][n-1]
dp[0][n-1] = arr[0][n-1]

for i in range(n-2,-1,-1) :
    dp[0][i] = dp[0][i+1] + arr[0][i]

for i in range(1,n) :
    dp[i][n-1] = dp[i-1][n-1] + arr[i][n-1]

#초기값 세팅후 dp 만들기 
for i in range(1,n) : 
    for j in range(n-2,-1,-1) :
        dp[i][j] = min(dp[i][j+1] + arr[i][j], dp[i-1][j] + arr[i][j])
 

print(dp[n-1][0])