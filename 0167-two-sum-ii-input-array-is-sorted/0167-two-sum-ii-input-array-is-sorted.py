class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}

        for i in range(len(numbers)):
            sub = target - numbers[i]
            if sub in h:
                return [h[sub]+1,i+1]
            else:
                h[numbers[i]] = i