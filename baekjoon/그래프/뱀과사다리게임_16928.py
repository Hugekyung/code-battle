# 뱀과 사다리 게임
# 주사위로 이동 가능한 칸 1~6
# 게임판 10 x 10
# 특정 위치로 이동하게 하는 사다리 및 뱀 시스템
# 칸: 위치(x, y) 형태의 딕셔너리

from collections import deque

def bfs(odd_dic):
    odd_keys = [key for key, _ in odd_dic.items()]
    dq = deque()
    dq.append((1, 0))
    visited = set()
    while dq:
        now, cnt = dq.popleft()
        for i in range(1, 7):
            nx = now + i
            if nx == 100:
                return cnt + 1
            elif nx < 0 or nx > 100:
                continue
            if nx not in visited:
                if nx in odd_keys:
                    idx = odd_keys.index(nx)
                    nx = odd_dic[odd_keys[idx]]
                dq.append((nx, cnt + 1))
                visited.add(nx)

n, m = map(int, input().split())
odd_dic = {}
for _ in range(n+m):
    x, y = map(int, input().split())
    odd_dic[x] = y
print(bfs(odd_dic))