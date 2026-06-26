class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = len(nums)

        num=[i for i in range(1,len(nums)+1)]
        lis = list((set(num) - set(nums)))
        return lis