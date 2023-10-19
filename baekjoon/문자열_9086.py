# 백준 - 문자열 9086번

n = int(input())
for _ in range(n):
    test_case = str(input())
    first = test_case[0]
    last = test_case[-1]
    print(first + last)