class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}

        for n in nums:
            h[n] = h.get(n,0)+1
        
        for key in h.keys():
            if h[key] == 1:
                return key
        
