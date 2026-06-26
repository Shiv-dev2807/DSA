class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}

        for n in nums:
            h[n] = h.get(n,0)+1
        
        l = list(h.values())
        m=(max(l))
        
        rev = {v:k for k,v in h.items()}
        return rev[m]