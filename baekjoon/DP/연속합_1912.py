import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
prefix_sum = [0] * (n + 1)
    
# 부분합 배열 계산
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]

# 부분합
# i ~ j 구간의 합은 부분한 j번 째 - i번 째
# 그 부분합들의 가장 큰 값을 반환
max_sum = -100000
for i in range(n):
    for j in range(i + 1, n):
        print(i, j)
        sub_arr_sum = prefix_sum[j] - prefix_sum[i]
        # print(max_sum, sub_arr_sum)
        max_sum = max(max_sum, sub_arr_sum)

print(max_sum)