# 색종이자르기 2630번
# 2024-10-19
# 종이의 색이 모두 같은 색이 아닐 때 -> 똑같은 크기의 4개 색종이로 자른다
# 자른 종이의 색이 모두 같은 색이 될 때까지 반복(재귀)
# 종료조건: 종이의 색이 모두 같은 색일 때(1 or 0)

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
paper_cnt = { 0: 0, 1: 0 }
def cut_paper(x, y, n, paper_cnt):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] == paper[x][y]: # 0,0 위치의 색과 같은지 확인
                continue
            else:
                # 색이 다름 -> 색종이 자르기
                cut_paper(x, y, n//2, paper_cnt) # 1사분면
                cut_paper(x, y + n//2, n//2, paper_cnt) # 2사분면
                cut_paper(x + n//2, y, n//2, paper_cnt) # 3사분면
                cut_paper(x + n//2, y + n//2, n//2, paper_cnt) # 4사분면
                return
    
    # 종이의 색이 모두 같음
    if paper[x][y] == 1: # 파란색
        paper_cnt[1] += 1
    else: # 하얀색
        paper_cnt[0] += 1
    return

cut_paper(0, 0, n, paper_cnt)
print(paper_cnt[0])
print(paper_cnt[1])

# 2회차 풀이
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0]

def cut_paper(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[x][y] != arr[i][j]:
                cut_paper(x, y, n//2)
                cut_paper(x, y + n//2, n//2)
                cut_paper(x + n//2, y, n//2)
                cut_paper(x + n//2, y + n//2, n//2)
                return
    
    if arr[x][y] == 0:
        result[0] += 1
    else:
        result[1] += 1
    return

cut_paper(0, 0, n)
print(result[0])
print(result[1])