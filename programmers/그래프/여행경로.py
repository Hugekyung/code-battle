# 1회차 - BFS
from collections import deque
import copy

def solution(tickets):
    tickets.sort(key = lambda x: x[1]) # 알파벳 순 정렬
    dq = deque()
    dq.append((['ICN'], tickets))
    while dq:
        path, left = dq.popleft()
        if not len(left):
            return pathdudfeijfe
        
        for i, [st, end] in enumerate(left):
            new_path = path.copy()
            new_left = left.copy()
            if path[-1] == st:
                new_path.append(end)
                new_left.pop(i)
                dq.append((new_path, new_left))