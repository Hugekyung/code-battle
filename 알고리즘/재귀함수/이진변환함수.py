# 10진수를 2진수로 변환하는 함수

arr = []
def number_to_binary(n, arr):
    v = n // 2 # 몫
    m = n % 2 # 나머지
    arr.append(m)
    if v == 0: # 더 이상 나눠지지 않을 때
        return arr
    else:
        return number_to_binary(v, arr)
    
print("".join(map(str, number_to_binary(10, arr)[::-1])))