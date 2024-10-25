# 쿼드트리 2회차 풀이
n = int(input())
arr = [str(input()) for _ in range(n)]
result = ""

def quad_tree(x, y, n):
    global result
    same_flag = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != arr[x][y]: # (x, y) 좌표의 색과 같은지 확인
                smae_flag = False
                result += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y, n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                result += ")"
                return
    
    if same_flag:
        result += str(arr[x][y])

quad_tree(0, 0, n)
print(result)