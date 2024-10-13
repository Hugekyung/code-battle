# 그룹 단어 체커 1316번

n = int(input())
group_count = 0
for _ in range(n):
    word = str(input())
    already_arr = set()
    flag = True
    for i in range(len(word)):
        w = word[i]
        if i == 0:
            already_arr.add(w)
            continue
        if w in already_arr and word[i-1] != w: # 이미 가지고 있는 w 중 직전 인덱스의 값이 w와 다른 경우(연속하지 않는 것으로 판단)
            flag = False
            break
        already_arr.add(w)
    if flag:
        group_count += 1

print(group_count)