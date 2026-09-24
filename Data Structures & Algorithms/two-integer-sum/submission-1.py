class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for idx,num in enumerate(nums):
            if target-num in map:
                x = map[target-num]
                return [x, idx]
            else:
                map[num] = idx
            
        