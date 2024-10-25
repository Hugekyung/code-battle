# 영화감독 숌 1436번
# 브루트포스 -> 666에서 시작해서 1씩 증가하며 666이 들어간 숫자를 찾을 때마다 cnt를 늘리고, n과 일치하는 값을 찾는다

def get_number(n):
    number = 666
    cnt = 0

    while True:
        if '666' in str(number):
            cnt += 1
        if cnt == n:
            print(number)
            return
        number += 1

n = int(input())
get_number(n)