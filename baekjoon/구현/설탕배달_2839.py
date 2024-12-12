# 3kg, 5kg 옵션
# Nkg을 만들 수 있는 최소 봉지의 개수
# 3 <= N <= 5000

def get_cnt(n):
    result = 0
    while n > 0:
        if n % 5 == 0:
            result += n // 5
            return result
        n -= 3
        result += 1
    if n != 0:
        return -1
    return result

n = int(input())
print(get_cnt(n))