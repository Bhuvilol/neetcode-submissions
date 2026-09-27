class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, len(nums)-1, 0
        while(k<=j):
            if nums[k] == 0:
                nums[i], nums[k] = nums[k], nums[i]
                i+=1
                k+=1
            elif nums[k] == 1:
                k+=1
            else:
                nums[k], nums[j] = nums[j], nums[k]
                j-=1
        