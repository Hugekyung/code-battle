class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 반복문 돌면서 같은 anagrams 그룹을 찾아 딕셔너리에 저장하고, 각 딕셔너리를 result 배열에 최종 추가
        dict = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if dict.get(key):
                dict[key].append(s)
            else:
                dict[key] = [s]
        return [val for _, val in dict.items()]