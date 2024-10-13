# 나머지 3052번

unique_set = set()
for _ in range(10):
    n = int(input())
    na = n % 42
    unique_set.add(na)

print(len(unique_set))

# 헤이밥 풀이
# 모듈 1: 10개의 숫자 배열 -> 각 숫자를 42로 나눈 배열 생성
arr = [int(input()) for _ in range(10)]
arr_42 = list(map(lambda elem: elem % 42, arr))

# 모듈 2: arr_42 -> 고유한 숫자들만 남긴 배열 생성
arr_42_unique = list(set(arr_42))

# 모듈 3: arr_42_unique -> 해당 배열의 개수 출력
print(len(arr_42_unique))