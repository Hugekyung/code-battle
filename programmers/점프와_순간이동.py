def solution(n):
    cnt = 0
    while n > 0:
        if n % 2 == 0:
            n = n//2
            continue
        n -= 1
        cnt += 1
        
    return cnt
        