# 모음의 개수 1264번

mo = ['a', 'e', 'i', 'o', 'u']
while True:
    count = 0
    words = input()
    if words == "#":
        break
    for w in words:
        if w.lower() in mo:
            count += 1
    print(count)