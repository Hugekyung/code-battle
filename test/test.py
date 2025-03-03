import sys

def solution(A, K):
    max_len = max([len(str(i)) for i in A])
    rows = "+" + "-" * max_len
    if K >= len(A): # 한 줄 처리
        sys.stdout.write(rows * len(A) + "+\n")
        sys.stdout.write("|" + "|".join(f"{num:>{max_len}}" for num in A) + "|\n")
        sys.stdout.write(rows * len(A) + "+\n")
    else: # K 개수마다 줄바꿈
        sys.stdout.write(rows * K + "+\n")
        row_check = 0
        for i, num in enumerate(A):
            if row_check == K:
                sys.stdout.write("|\n")
                sys.stdout.write(rows * K)
                sys.stdout.write("+\n")
                row_check = 0
            row_check += 1
            sys.stdout.write("|" + f"{num:>{max_len}}")
            if i == len(A) - 1:
                sys.stdout.write("|\n")
                sys.stdout.write(rows * row_check + "+")
            

solution([4, 35, 80, 123, 12345, 44, 8, 5], 10)
print()
solution([4, 35, 80, 123, 12345, 44, 8, 5, 24, 3], 4)
print()
solution([4, 35, 80, 123, 12345, 44, 8, 5, 24, 3, 22, 35], 4)