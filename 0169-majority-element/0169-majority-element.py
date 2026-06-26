class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}

        for n in nums:
            h[n] = h.get(n,0)+1
        
        l = max(list(h.values()))

        for key, value in h.items():
            if value == l:
                return key
        