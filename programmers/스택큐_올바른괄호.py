def solution(s):
    stack = []
    for val in s:
        if val == "(":
            stack.append(val)
        else:
            if stack == []:
                return False
            elif val == ")":
                stack.pop()
            
    return stack == []