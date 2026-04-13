class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                area = min(heights[i], heights[j]) * (j - i)
                
                if area > maxArea:
                    maxArea = area
        return maxArea
        