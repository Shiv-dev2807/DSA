class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = 0

        lpos = []
        lneg=[]
        outputnums = []

        for i in range(len(nums)):
            if nums[i] > 0:
                lpos.append(nums[i])
            else:
                lneg.append(nums[i])
            
            i+=1
        
        while left<len(lpos):
            outputnums.append(lpos[left])
            outputnums.append(lneg[right])
            left+=1
            right+=1
        
        return outputnums