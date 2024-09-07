h, m = map(int, input().split(' '))
cook_min = int(input())

# 1. 주어진 요리 시간을 시 + 분 단위로 계산
c_h = cook_min // 60
c_m = cook_min % 60

# 2. 분 단위 먼저 계산
cal_round_h = (c_m + m) // 60
cal_m = (c_m + m) % 60

# 3. 시 단위 계산
end_h = h + c_h + cal_round_h # 최종 종료 시
end_m = cal_m # 최종 종료 분

if end_h > 24:
    end_h = end_h - 24
elif end_h == 24:
    end_h = 0

print(f"{end_h} {end_m}")