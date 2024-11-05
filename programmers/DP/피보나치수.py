# dp로 풀어야되는듯
def solution(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2])
        
    return dp[n] % 1234567

# 2회차 풀이
# 점화식: fibo(n) = fibo(n-1) + fibo(n-2)
# fibo(1) = 1
def solution(n):
    if n == 1: return 1 % 1234567
    dp = [0] * (n+1)
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n] % 1234567