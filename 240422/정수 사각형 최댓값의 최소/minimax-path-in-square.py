n = int(input())
arr = []
for i in range(n) : 
    arr.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
# 초기값 세팅
dp[0][0] = arr[0][0]

# 첫 번째 열 초기화
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], arr[i][0])

# 첫 번째 행 초기화
for j in range(1, n):
    dp[0][j] = max(dp[0][j-1], arr[0][j])

# 나머지 셀들에 대한 계산
for i in range(1, n):
    for j in range(1, n):
        # 현재 셀에 도달하기 위한 두 경로 중 더 작은 최대값을 선택하고, 현재 셀의 값을 고려
        dp[i][j] = max(min(dp[i-1][j], dp[i][j-1]), arr[i][j])

print(dp[n-1][n-1])