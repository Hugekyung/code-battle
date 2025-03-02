# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    positiveArr = [val for val in set(A) if val > 0]
    if positiveArr == []:
        return 1
    for i, v in enumerate(sorted(positiveArr)):
        if i+1 == v:
            continue
        return i+1
    else:
        return v+1