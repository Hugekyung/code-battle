# 플로이드 - 11404번
# 플로이드-워셜 알고리즘: 가능한 모든 노드 쌍에 대해 최단 거리를 구하는 알고리즘

import sys
INF = float('inf')

def floyd(n, graph):
    # 플로이드-워셜
    for k in range(n): # 경유 노드
        for i in range(n): # 출발 노드
            for j in range(n): # 도착 노드
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                print(0, end=" ")
            else:
                print(graph[i][j], end=" ")
        print()

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[INF] * n for _ in range(n)] # 그래프 초기화
for i in range(n):
    graph[i][i] = 0 # 자기 자신으로 가는 비용은 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    graph[a][b] = min(graph[a][b], c)

floyd(n, graph)