class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h={}
        i = 1
        j = 0

        while i < len(nums):
            if nums[i] == nums[j]:
                i+=1
            else:
                j+=1
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
        
        return len(nums[:j+1])