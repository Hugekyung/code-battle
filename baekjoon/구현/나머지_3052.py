# 나머지 3052번

unique_set = set()
for _ in range(10):
    n = int(input())
    na = n % 42
    unique_set.add(na)

print(len(unique_set))