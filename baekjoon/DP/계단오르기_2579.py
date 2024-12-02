# 한번에 1 or 2 계단
# 밟은 계단의 점수를 합산하여 갖게 된다
# 연속된 3개 계단은 밟으면 안된다(시작점은 예외)
# 마지막 계단은 반드시 밟아야 한다

def up_stairs(dp, s, n):
    for i in range(3, n+1):
        # n-1번째 계단에서 오는 경우 -> dp의 [i-3] 위치의 최댓값 + 직전 계단의 점수 + i번째 계단의 점수
        # n-2번째 계단에서 오는 경우 -> dp의 [i-2] 위치의 최댓값 + i번째 계단의 점수
        dp[i] = max(dp[i-3] + s[i-1] + s[i], dp[i-2] + s[i])
    return dp[n]

n = int(input())
s = [0] + [int(input()) for _ in range(n)]
dp = [0] * (n+1)

if n == 1:
    print(s[1])
elif n == 2:
    print(s[1] + s[2])
else:
    dp[1] = s[1]
    dp[2] = dp[1] + s[2]
    print(up_stairs(dp, s, n))