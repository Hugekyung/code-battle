from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # t가 s의 anagram이면 true, 아니면 false 반환?
        if len(s) != len(t):
            return False
        dic = defaultdict(int)
        for a in s:
            dic[a] += 1
        for b in t:
            if dic[b] - 1 < 0:
                return False
            dic[b] -= 1
        return True
