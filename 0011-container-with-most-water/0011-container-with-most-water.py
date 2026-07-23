class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1

        max_amount_of_water = 0

        while l < r:
            width = r - l
            heigh = min(height[l],height[r])

            area = width * heigh

            if area > max_amount_of_water:
                max_amount_of_water = area
            
            if heigh == height[l]:
                l+=1
            else:
                r-=1
        
        return max_amount_of_water