class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        for n in nums:
            h[n] = h.get(n,0)+1
        
        lmaj = []
        for key in h.keys():
            if h[key] > (len(nums)//3):
                lmaj.append(key)
        
        return lmaj