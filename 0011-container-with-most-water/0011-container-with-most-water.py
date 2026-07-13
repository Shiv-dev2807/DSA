class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1

        max_amount_of_water = 0

        while left < right:
            width = right - left
            heigh = min(height[left],height[right])

            area = width * heigh

            if area > max_amount_of_water:
                max_amount_of_water = area
            
            if heigh == height[left]:
                left+=1
            else:
                right-=1
        
        return max_amount_of_water