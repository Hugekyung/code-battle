# 1260번 - DFS와 BFS

from collections import deque

def dfs(result, arr, v):
    return

def bfs(arr, v):
    result = [str(v)]
    print(arr) # debug
    dq = deque([v])
    while dq:
        idx = dq.popleft()
        print(idx)
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

# print(dfs(result, arr, v))
print(bfs(arr, v))