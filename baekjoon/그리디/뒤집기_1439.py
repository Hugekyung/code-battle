# 뒤집기 - 1439번
# 연속된 문자열을 0 또는 1로 뒤집어 전체 문자열을 0 혹은 1로 이루어진 문자열로 만들기
# 전부 0으로 만드는 과정 count, 1로 만드는 과정 count 중 작은 count 반환

def main(S):
    if "1" not in S:
        return 0
    elif "0" not in S:
        return 0
    return counter(S)

def counter(S):
    cnt_z = 0
    cnt_o = 0
    if S[0] == "0":
        cnt_z += 1
    else:
        cnt_o += 1
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            if S[i+1] == "0":
                cnt_z += 1
            else:
                cnt_o += 1     
    return min(cnt_z, cnt_o)

S = input()
print(main(S))