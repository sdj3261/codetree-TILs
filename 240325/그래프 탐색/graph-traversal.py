n, m = map(int, input().split())
tree = {}
visited = [False] * (n + 1)
q = [1]
visited[1] = True
result = 0

for _ in range(m):
    s, e = map(int, input().split())
    # s와 e 노드를 tree에 양방향으로 추가하는 과정 간소화
    tree.setdefault(s, []).append(e)
    tree.setdefault(e, []).append(s)

while q:
    curr = q.pop(0)  # 큐의 첫 번째 요소를 제거하여 현재 노드로 설정
    result += 1  # 방문한 노드의 수를 증가

    for v in tree.get(curr, []):  # curr에서 이동할 수 있는 모든 노드 v에 대해
        if not visited[v]:  # 아직 방문하지 않은 노드라면
            visited[v] = True  # 방문 처리
            q.append(v)  # 큐에 추가

# 1번 노드 자체를 제외하고 연결된 노드의 수를 계산하기 때문에 -1을 해줍니다.
print(result - 1)