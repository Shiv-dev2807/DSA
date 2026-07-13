class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for n in nums:
            h[n] = h.get(n,0)+1
        
        lt = sorted(h.items(), key=lambda x: x[1], reverse=True)

        l = []

        for i in range(k):
            l.append(lt[i][0])
        
        return(l)