class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,num in enumerate(nums):
            if target-num in map:
                return [seen[target-num], idx]
            else:
                seen[num] = idx
        return -1
        