def calculateMaxScore(user, m):
    ret = 0
    for i in user :
        if i >= m :
            ret +=1
    return ret

def yoot(turn, user, m, cnt):
    global max_ret
    max_ret = max(max_ret, calculateMaxScore(user, m))
    if cnt == len(turn):
        return
    for i in range(len(user)):
        if user[i] >= m :
            continue

        user[i] += turn[cnt]
        yoot(turn, user, m, cnt+1)
        user[i] -= turn[cnt]



n, m, k = map(int, input().split())
turn = list(map(int, input().split()))

max_ret = 0
user = [1] * k  # 모든 말은 1번 위치에서 시작

yoot(turn, user, m, 0)  # 모든 턴에 대해 재귀적으로 처리
print(max_ret)