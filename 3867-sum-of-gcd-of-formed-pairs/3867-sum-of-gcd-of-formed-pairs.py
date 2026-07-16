import math
class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mxi = 0
        l1 = []
        for i in range(len(nums)):
            if nums[i] > mxi:
                mxi = nums[i]
            
            prefixGcd = math.gcd(nums[i],mxi)
            l1.append(prefixGcd)
        
        l1 = sorted(l1)
        left = 0
        right = len(l1)-1
        l2=[]
        while left < right:
            l2.append(math.gcd(l1[left],l1[right]))
            left+=1
            right-=1
        
        return(sum(l2))