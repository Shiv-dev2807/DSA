class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """h = {}

        for n in nums:
            h[n] = h.get(n,0)+1
        
        l = max(h.values())

        for key, value in h.items():
            if value == l:
                return key"""
        
        can = nums[0]
        count = 1

        for i in range(1,len(nums)):
            if count != 0:
                if nums[i] == can:
                    count+=1
                else:
                    count-=1
            else:
                can = nums[i]
                count+=1
        
        return can
            