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