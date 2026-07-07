class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        l = [x for x in nums if x >= 0]
        l1 =[x for x in nums if x<0]

        if l and l1:
            if abs(max(l1)) > min(l):
                return min(l)
            elif abs(max(l1)) < min(l):
                return max(l1)
            elif abs(max(l1)) == min(l):
                return min(l)
        elif l and not l1:
            return min(l)
        elif l1 and not l:
            return max(l1)
        else:
            return 0