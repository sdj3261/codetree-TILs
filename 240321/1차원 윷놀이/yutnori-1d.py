def calculateMaxScore(user, m):
    return sum(1 for position in user if position == m)

def yoot(turn, user, m, num):
    global max_ret
    if num == 0:
        max_ret = max(max_ret, calculateMaxScore(user, m))
        return
    for i in range(len(user)):
        if user[i] < m:  # m에 도달하지 않은 말만 이동
            original_position = user[i]
            for j in turn:
                user[i] += j
                if user[i] > m:  # m을 넘어서면 안 되므로 체크
                    user[i] = m
                yoot(turn, user, m, num-1)
                user[i] = original_position  # 말의 위치를 원래대로 되돌림

n, m, k = map(int, input().split())
turn = list(map(int, input().split()))

max_ret = 0
user = [1] * k  # 모든 말은 1번 위치에서 시작

yoot(turn, user, m, n)  # 모든 턴에 대해 재귀적으로 처리
print(max_ret)