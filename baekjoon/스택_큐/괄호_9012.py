n = int(input())
for _ in range(n):
    case = str(input())
    if len(case) % 2 != 0:
        print("NO")
        continue
    elif case[-1] == "(" or case[0] == ")":
        print("NO")
        continue

    stack = []
    is_valid = True
    for c in case:
        if c == "(":
            stack.append(c)
        elif stack != [] and c == ")":
            stack.pop()
        elif stack == [] and c == ")":
            is_valid = False
            break

    if is_valid == True and len(stack) == 0:
        print("YES")
    else:
        print('NO')