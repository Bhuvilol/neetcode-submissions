def twosumhelper(f :int, nums:list[int], target: int, results: list[list[int]]):
    i = f+1
    j = len(nums) - 1
    while(i<j):
        current_sum = nums[i] + nums[j]
        if current_sum == target:
            results.append([nums[f], nums[i], nums[j]])
            i += 1
            j -= 1
            
            while i < j and nums[i] == nums[i - 1]:
                i += 1
            while i < j and nums[j] == nums[j + 1]:
                j -= 1
        elif current_sum < target:
            i += 1
        else:
            j -= 1


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            twosumhelper(i, nums, -nums[i], results)
            
        return results