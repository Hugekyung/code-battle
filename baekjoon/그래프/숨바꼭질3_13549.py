# 숨바꼭질 3 - 13549번
# 이동 방법
# 1초 후 -1 or +1
# 0초 후 *2
# 최단 시간

from collections import deque

def bfs(n, k):
    dq = deque()
    dq.append((n, 0)) # 출발지점, 소요시간(초)
    max_pos = max(2*k, n)
    visited = [0] * (max_pos + 1)
    while dq:
        x, sec = dq.popleft()
        if x == k:
            return sec
        
        nx = x * 2
        if nx <= max_pos and not visited[nx]:
            visited[nx] = 1
            dq.appendleft((nx, sec)) # 시간이 0초 소요되니까 맨 왼쪽으로 삽입

        for d in (-1, 1):
            nx = x + d
            if 0 <= nx <= max_pos and not visited[nx]:
                visited[nx] = 1
                dq.append((nx, sec + 1))

n, k = map(int, input().split())
print(bfs(n, k))