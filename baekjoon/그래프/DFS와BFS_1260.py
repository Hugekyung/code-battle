# 1260번 - DFS와 BFS

from collections import deque

def dfs(arr, v):
    visited = []
    dq = deque([v])
    while dq:
        node = dq.pop()
        if str(node) not in visited:
            visited.append(str(node))
            dq.extend(sorted(arr[node], reverse=True))
    return " ".join(visited)

def bfs(arr, v):
    result = [str(v)]
    dq = deque([v])
    while dq:
        idx = dq.popleft()
        for j in sorted(arr[idx]):
            if str(j) not in result:
                result.append(str(j))
                dq.append(j)
    return " ".join(result)

n, m, v = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

print(dfs(arr, v))
print(bfs(arr, v))