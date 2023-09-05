class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_water = 0
        while i != j:
            if height[i] < height[j]:
                container_water = height[i] * (j - i)
                if container_water > max_water:
                    max_water = container_water
                i += 1
            elif height[i] >= height[j]:
                container_water = height[j] * (j - i)
                if container_water > max_water:
                    max_water = container_water
                j -= 1
        return max_water
        