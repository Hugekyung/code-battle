# 2163 - 카드2
from collections import deque

n = int(input())
dq = deque([i for i in range(1, n+1)])

while len(dq) > 1:
    dq.popleft() # 맨 앞 버리기
    dq.append(dq.popleft()) # 맨 앞의 값을 맨 뒤로

if len(dq) == 1:
    print(dq.pop())