# 피보나치 수 - 재귀호출 버전
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(int(input())))