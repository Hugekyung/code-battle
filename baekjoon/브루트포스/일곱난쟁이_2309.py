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


# 5회차 풀이
from itertools import permutations

arr = sorted([int(input()) for _ in range(9)])
cases = permutations(arr, 7)
for case in cases:
    if sum(case) == 100:
        for c in case:
            print(c, end="\n")
        break

# 2309 - 일곱 난쟁이 - 6회차 풀이
# 먼저 선정렬 -> 2중 for문을 돌며 2개를 뺐을 때 합이 100인 두 수의 경우의 수 탐색 -> 찾으면 반환
arr = [int(input()) for i in range(9)]
arr.sort()
s = sum(arr)

def finds():
    for i in range(9):
        for j in range(i+1, 9):
            if s - arr[i] - arr[j] == 100:
                for num in arr:
                    if num == arr[i] or num == arr[j]:
                        continue
                    else:
                        print(num, end="\n")
                return

finds()     