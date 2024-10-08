# DP 익숙해지는 팁
# 1. 브루트포스처럼 풀이하고,
# 2. 이걸 메모이제이션으로 어떻게 시간복잡도를 줄일 수 있을지 고민하기
# 3. 재귀 -> DP

# <아이디어>
# 가장 적은 횟수인 것부터 계산하고, 이미 계산한 것을 저장해뒀다가 재활용

import sys

x = int(sys.stdin.readline())

dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1 # 1을 빼는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])