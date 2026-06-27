class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = nums[i] * -1
        

        s = 0
        e = len(nums)-1

        while e >= s:
            if nums[s]**2 > nums[e]**2:
                nums[s],nums[e] = nums[e],nums[s]**2
                e-=1
            else:
                nums[e] = nums[e]**2
                e-=1
        

        return(sorted(nums))