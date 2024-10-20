import sys

n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    case = list(map(int, sys.stdin.readline().split()))
    order = case[0]

    if order == 1:
        stack.append(case[1])
    elif order == 2:
        if stack != []:
            print(stack.pop())
        else:
            print(-1)
    elif order == 3:
        print(len(stack))
    elif order == 4:
        if stack == []:
            print(1)
        else:
            print(0)
    elif order == 5:
        if stack != []:
            print(stack[-1])
        else:
            print(-1)
