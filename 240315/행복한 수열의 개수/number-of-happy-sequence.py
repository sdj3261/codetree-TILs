def count_seq(arr, m):
    ret = 0
    max_ret = 0
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            ret = ret + 2 if ret == 0 else ret + 1
        else:
            ret = 0
        max_ret = max(max_ret, ret)
    return max_ret >= m

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

if m == 1:
    print(2 * n)  # 각 행과 각 열 모두 최소 1의 길이를 가지므로, 2*n이 정답입니다.
else:
    ret = 0
    transposed_matrix = list(map(list, zip(*arr)))
    for data in arr + transposed_matrix:
        if count_seq(data, m):
            ret += 1
    print(ret)