# 스택 10828번
import sys

n = int(sys.stdin.readline())
stack = []
for _ in range(n):
    commands = list(map(str, sys.stdin.readline().split()))
    if commands[0] == "push":
        stack.append(commands[1])
    elif commands[0] == "pop":
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif commands[0] == "size":
        print(len(stack))
    elif commands[0] == "empty":
        if stack == []:
            print(1)
        else:
            print(0)
    else: # top
        if stack == []:
            print(-1)
        else:
            print(stack[-1])