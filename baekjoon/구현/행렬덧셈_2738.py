# 행렬 덧셈 2738번

n, m = map(int, input().split())
matrix_1 = [list(map(int, input().split())) for _ in range(n)]
matrix_2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_1[i][j] + matrix_2[i][j])
    
    print(*row)