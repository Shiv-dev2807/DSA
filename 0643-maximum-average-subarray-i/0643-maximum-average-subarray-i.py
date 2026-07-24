class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[0:k])
        a = sum(nums[0:k])/k
        ma = a

       
        right = k
        while right < len(nums):
            s += nums[right] - nums[right-k]
            a = s/k
            ma = max(ma,a)
            
            right+=1
        return ma