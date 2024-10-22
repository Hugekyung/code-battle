# 좌표 압축 18870번
# 아이디어: 자기 자신보다 작은 수의 개수는, 오름차순 정렬했을 때 자신의 인덱스와 같다
# 예) index가 2일 경우, 정렬했을 때 오름차순으로 2번째가 된 것이므로 자기 자신보다 작은 수는 2개다.

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
set_arr = list(sorted(set(arr)))
count_dict = {set_arr[i]: i for i in range(len(set_arr))}
for key in arr:
    print(count_dict[key], end=" ")