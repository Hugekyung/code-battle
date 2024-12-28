# 쿼드트리 1992번
n = int(input())
arr = [str(input()) for _ in range(n)]
res_arr = []

# 사분면을 자르는 함수
def cut_QT(x, y, n):
    global res_arr
    print('시작 => ', x, y, n)
    # 사분면의 값이 하나로 통일되는지 확인
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != arr[x][y]:
                res_arr.append("(")
                cut_QT(x, y, n//2)
                cut_QT(x, y + n//2, n//2)
                cut_QT(x + n//2, y, n//2)
                cut_QT(x + n//2, y + n//2, n//2)
                res_arr.append(")")
                return

    # 사분면의 모든 색이 같음
    res_arr.append(arr[x][y])

cut_QT(0, 0, n)
print("".join(res_arr))

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

# 쿼드트리 1992번 - 3회차 풀이
n = int(input())
arr = [str(input()) for _ in range(n)]

result = ""
def quad_tree(x, y, n):
    global result

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                result += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y, n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                result += ")"
                return

    result += arr[x][y]
    return

quad_tree(0, 0, n)
print(result)

# 3회차 풀이
n = int(input())
arr = [str(input()) for _ in range(n)]
result = ""

def quad_tree(x, y, n):
    global result
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[x][y] != arr[i][j]:
                result += "("
                quad_tree(x, y, n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result += ")"
                return

    if arr[x][y] == "1":
        result += "1"
    else:
        result += "0"
    return

quad_tree(0, 0, n)
print(result)

# 4회차 풀이
n = int(input())
arr = [input() for _ in range(n)]
result = ''

def quad_tree(x, y, n):
    global result
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:
                result += '('
                quad_tree(x, y, n//2)
                quad_tree(x, y + n//2, n//2)
                quad_tree(x + n//2, y, n//2)
                quad_tree(x + n//2, y + n//2, n//2)
                result += ')'
                return
    if arr[x][y] == '1':
        result += '1'
    else:
        result += '0'
    return

quad_tree(0, 0, n)
print(result)