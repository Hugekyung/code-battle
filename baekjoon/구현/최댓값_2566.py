# 최댓값 2566번
import sys

matrix = [list(map(int, sys.stdin.readline().split()))  for _ in range(9)]
max_value = int(-1e9)
max_i = 0
max_j = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_i = i
            max_j = j

print(max_value)
print(max_i+1, end=" ")
print(max_j+1)