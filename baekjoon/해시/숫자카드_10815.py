# 숫자 카드 10815번
import sys

n = int(sys.stdin.readline())
my_cards = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

for card in cards:
    if card in my_cards:
        print(1, end = " ")
    else:
        print(0, end = " ")