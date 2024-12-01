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

# 1로 만들기 2024-11-29 풀이
def make_one(dp, n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 1 # 1을 빼는 경우
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        
    return dp[n]

n = int(input())
dp = [0] * (n+1)
print(make_one(dp, n))

# 1로 만들기 2회차 풀이
n = int(input())
dp = [0] * (n+1)
for i in range(2, n+1):
    # 1을 뺄 때
    dp[i] = dp[i-1] + 1 # 1을 뻈을 때의 경우의 수보다 1 많음
    if i % 2 == 0:
        # 2로 나누어질 때(1을 뺐을 때와 어떤 것이 횟수가 더 적은지 비교)
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0: # 3으로 나눠질 때로 업데이트 해야하므로 if 조건으로 해야함
        # 3로 나누어질 때(1을 뺐을 때와 어떤 것이 횟수가 더 적은지 비교)
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])