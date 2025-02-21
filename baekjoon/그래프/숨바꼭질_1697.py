# 숨바꼭질 1697번
# 이동 방법 : -1, 1, x2
# dp도 가능은 할 것 같은데..?
# 우선은 bfs로..?

from collections import deque

def bfs(n, k):
    max_val = 100000
    visited = [0] * (max_val + 1)
    dq = deque()
    dq.append((n, 0))
    visited[n] = 1
    while dq:
        x, sec = dq.popleft()
        if x == k:
            return sec
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= max_val and not visited[nx]:
                dq.append((nx, sec+1))
                visited[nx] = 1

n, k = map(int, input().split())
print(bfs(n, k))