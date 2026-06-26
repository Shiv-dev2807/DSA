class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """l = len(nums)

        num=[i for i in range(1,len(nums)+1)]
        lis = list((set(num) - set(nums)))
        return lis"""
        """h = {}
        l = []
        for n in nums:
            h[n] = n
        
        for i in range(1,len(nums)+1):
            if i in h:
                continue
            else:
                l.append(i)
        
        return l"""
        
        l = [0]*len(nums)

        for n in nums:
            l[n-1]=1
        
        
        return [i+1 for i in range(len(l)) if l[i] == 0]