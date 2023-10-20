# 백준 - 다이얼 5622번
import sys

words = str(sys.stdin.readline())
spend_time = 0
for word in words:
    if word in "ABC":
        spend_time += 3
    elif word in "DEF":
        spend_time += 4
    elif word in "GHI":
        spend_time += 5
    elif word in "JKL":
        spend_time += 6
    elif word in "MNO":
        spend_time += 7
    elif word in "PQRS":
        spend_time += 8
    elif word in "TUV":
        spend_time += 9
    elif word in "WXYZ":
        spend_time += 10

print(spend_time)

