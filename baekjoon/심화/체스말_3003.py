arr = list(map(int, input().split(' ')))

result = []
white_arr = [1, 1, 2, 2, 2, 8]
for i, j in zip(arr, white_arr):
    if i == j:
        result.append(str(0))
    elif i > j:
        result.append(str(- (i - j)))
    elif i < j:
        result.append(str(j - i))

print(' '.join(result))