class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        p = k-1
        mA = 0
        s = 0
        while p < len(nums):
            if i == 0:
                for j in range(i,p+1):
                    s = s+nums[j]
                av = s/k
                mA = av
                i+=1
                p+=1
            else:
                s = s - nums[i-1] + nums[p]
                av = s/k
                if av > mA:
                    mA = av
                i+=1
                p+=1
        
        return(mA)
                