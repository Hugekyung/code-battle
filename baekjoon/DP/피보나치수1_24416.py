# 피보나치 수 - 재귀호출 버전
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(int(input())))

# DP 문제풀이
def fib_dp(n):
    a, b = 1, 1
    for _ in range(3, n+1):
        a, b = b, a + b # 값 스왑을 통해 직전 값 기억(직전 b값 -> a값)
    
    return b

