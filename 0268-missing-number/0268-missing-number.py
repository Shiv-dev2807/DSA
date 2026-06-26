class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        h = {}

        for n in nums:
            h[n] = n
        
        for i in range(1,len(nums)+1):
            if i not in h:
                return i
        
        return 0