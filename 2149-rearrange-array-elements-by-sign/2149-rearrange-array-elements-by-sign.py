class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = 0

        leven = []
        lodd=[]
        outputnums = []

        for i in range(len(nums)):
            if nums[i] > 0:
                leven.append(nums[i])
            else:
                lodd.append(nums[i])
            
            i+=1
        
        while left<len(leven):
            outputnums.append(leven[left])
            outputnums.append(lodd[right])
            left+=1
            right+=1
        
        return outputnums