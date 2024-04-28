n, m = map(int, input().split())
arr = []

# 입력 배열 구성
for i in range(n):
    arr.append(list(map(int, input().split())))

ret = -1

def is_rectangle(start_y, start_x):
    max_area = 0
    min_width = float('inf')
    
    # start_y, start_x에서 시작하여 가능한 최대 직사각형 찾기
    for y in range(start_y, n):
        if arr[y][start_x] <= 0:
            break
        width = 0
        while start_x + width < m and arr[y][start_x + width] > 0:
            width += 1
        min_width = min(min_width, width)
        current_area = min_width * (y - start_y + 1)
        max_area = max(max_area, current_area)
    
    return max_area

# 전체 배열을 순회하며 양수 시작점에서 직사각형 크기 계산
for i in range(n):
    for j in range(m):
        if arr[i][j] > 0:
            ret = max(ret, is_rectangle(i, j))

print(ret if ret > 0 else -1)