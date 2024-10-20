# 큐 10845번

import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque()

for _ in range(n):
    commands = list(map(str, sys.stdin.readline().split()))
    if commands[0] == "push":
        dq.append(commands[1])
    elif commands[0] == "pop":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif commands[0] == "size":
        print(len(dq))
    elif commands[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif commands[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    else:
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
