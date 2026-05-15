class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            find_num = target - num
            try:
                idx = nums.index(find_num)
                if i != idx:
                    res.append(i)
                    res.append(idx)
                    break
            except:
                continue
        return res