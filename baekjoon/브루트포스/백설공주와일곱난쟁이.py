# 백설 공주와 일곱 난쟁이 3040번
from itertools import combinations

arr = [int(input()) for _ in range(9)]
cases = list(combinations(arr, 7))
for c in cases:
    if sum(c) == 100:
        for r in c:
            print(r, end="\n")
        break