class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        maxCurrent = 0
        for i in range(len(arr)-1,-1,-1):
            current = arr[i]
            arr[i] = maxCurrent

            if maxCurrent < current:
                maxCurrent = current
            
            
        
        arr[-1] = -1
        return arr