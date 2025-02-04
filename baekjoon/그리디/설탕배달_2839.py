def get_min_cnt(n):
    cnt = 0
    while n > 0:
        if 0 < n < 3: return -1
        if n % 5 == 0:
            cnt += n // 5 
            n = n % 5
        else:
            n -= 3
            cnt += 1
    return cnt

n = int(input())
print(get_min_cnt(n))