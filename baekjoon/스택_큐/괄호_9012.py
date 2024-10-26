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

# 2회차 풀이 2024-10-26
# 괄호 9012번 2회차 풀이
# 스택
n = int(input())
for _ in range(n):
    ps = str(input())
    stack = [] # (만 들어가는 스택
    flag = True
    for p in ps:
        if p == "(":
            stack.append(p)
        else:
            if stack == []:
                print("NO")
                flag = False
                break
            else:
                stack.pop()
    if flag:
        if len(stack) > 0:
            print("NO")
        elif stack == []:
            print("YES")