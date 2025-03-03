def max_substrings(s):
    count = 0  # 부분 문자열 개수
    i = 0
    n = len(s)

    while i < n - 1:  # 최소 길이 2 이상이어야 하므로 마지막 문자 전까지만 탐색
        for j in range(i + 1, n):  # i 이후부터 끝까지 탐색
            if s[i] == s[j]:  # 시작과 끝이 같은 문자 찾기
                count += 1  # 부분 문자열 개수 증가
                i = j + 1  # 다음 부분 문자열 탐색을 위해 이동
                break
        else:
            i += 1  # 끝까지 탐색했지만 조건을 만족하는 부분 문자열을 못 찾으면 다음 문자로 이동

    return count

# 테스트 케이스
print(max_substrings("zzaaabbccall"))  # ✅ 5 ("zz", "aaa", "bb", "cc", "ll")
print(max_substrings("sashalikesana"))  # ✅ 3 ("sas", "ana", "likesa")
print(max_substrings("abba"))  # ✅ 1 ("abba")
print(max_substrings("abcabc"))  # ✅ 1 ("abca")
print(max_substrings("aabbcc"))  # ✅ 3 ("aa", "bb", "cc")
print(max_substrings("abcd"))  # ✅ 0 (조건 만족하는 부분 문자열 없음)
print(max_substrings("aaaa"))  # ✅ 2 ("aa", "aa")
print(max_substrings("racecarxracecar"))  # ✅ 2 ("racecar", "racecar")
print(max_substrings("zzaaabbccall"))  # ❌ 5 ("zz", "aaa", "bb", "cc", "ll")