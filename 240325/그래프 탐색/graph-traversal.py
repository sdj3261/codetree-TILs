n,m = map(int,input().split())
tree = {}
visited = [False for _ in range(n+1)]
q = []
ret = set()
ret.add(1)

for i in range(m) :
    s,e = map(int,input().split())

    if s in tree :
        tree[s].append(e)
    if s not in tree :
        tree[s] = [e]

    if e in tree :
        tree[e].append(s)
    if e not in tree :
        tree[e] = [s]

if tree and 1 in tree :
    q.append(1)
    visited[1] = True

while q :
    curr = q.pop()

    for v in tree[curr] :
        if not visited[v] :
            ret.add(v)
            q.append(v)
            visited[curr] = True

if 1 in ret :
    result = len(ret) - 1
else :
    result = len(ret)
    

print(result)