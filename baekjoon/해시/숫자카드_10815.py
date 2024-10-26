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

# 숫자 카드 10815번 2회차 풀이
# 해시
n = int(input())
set_my_card = set(list(map(int, input().split())))
m = int(input())
cards = list(map(int, input().split()))
for card in cards:
    if card in set_my_card:
        print(1, end=" ")
    else:
        print(0, end=" ")
