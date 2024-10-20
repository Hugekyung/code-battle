# 일곱 난쟁이 2309번
# 브루트포스/정렬
from itertools import permutations

arr = [int(input()) for _ in range(9)]
arr.sort() # 키를 오름차순 정렬

def picker(arr, s): # s: 선택하고자 하는 개수
    cases = permutations(arr, 7)
    for case in cases:
        if sum(case) == 100:
            return case

# 9명 중 7명을 뽑는 경우의 수 구하기(9C7)
# 경우의 수를 탐색하여 합이 100인 경우의 수 구하기
# 오름차순 순서대로 출력
res = picker(arr, 7)
for i in range(len(res)):
    print(res[i], end="\n")