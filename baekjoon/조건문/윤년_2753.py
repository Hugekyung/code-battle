# 윤년이면 1, 아니면 0 출력
# 윤년은 4의 배수 + 100의 배수가 아닐 때 / 400의 배수일 때

year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)