# 피보나치 수열하고 같음
# 처음에는 재귀로 풀이했으나 시간초과로 DP 풀이

def solution(n):
    if n == 1:
        return 1 % 1234567
    elif n == 2:
        return 2 % 1234567
    
    dp = [0 for _ in range(n+1)]
    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n] % 1234567