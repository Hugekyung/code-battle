# x 보다 작은 수 세기 10871번
n, x = map(int, input().split())
arr = list(map(int, input().split()))
for i in arr:
    if i < x:
        print(i, end=" ")