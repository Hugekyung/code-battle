# 백준 - 단지번호 붙이기 2667번
# dfs -> 모든 시작점으로부터 연결된 집의 개수를 list에 저장

from collections import deque
import copy

def bfs(i, j, arr):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    dq = deque((i, j))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 1:
                

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
result = []
visited = arr.copy()
for i in range(n):
    for j in range(n[i]):
        if visited[i][j] == 1:
            visited[i][j] = 0
            bfs(i, j, arr)