class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 in nums:
            s = nums.index(0)
        else:
            s = -1
        e = -1

        
        
        for j in range(len(nums)):
            if nums[j] != 0 and j > s:
                e = j
                break
    
        while s != len(nums) and e != len(nums) and s<=e:
            if nums[s] == 0 and nums[e] != 0:
                nums[s], nums[e] = nums[e], nums[s]
                s+=1
                e+=1
            elif nums[s] !=0:
                s+=1
            elif nums[e] ==0:
                e+=1
            