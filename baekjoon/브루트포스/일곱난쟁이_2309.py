###### 일곱 난쟁이 2309번 ######
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

###### 일곱난쟁이 2309번 4회차 풀이 ######
# 시간 제한 2초 -> 파이썬 기준 1초 2,000만번 -> 총 4,000만번 가능
import sys

arr = sorted([int(sys.stdin.readline()) for _ in range(9)])
sum_arr = sum(arr)
is_break = False
for i in range(len(arr)):
    if is_break: break
    for j in range(i+1, len(arr)):
        if sum_arr - arr[i] - arr[j] == 100:
            for k in arr:
                if k == arr[i] or k == arr[j]:
                    continue
                else:
                    print(k, end="\n")
            is_break = True