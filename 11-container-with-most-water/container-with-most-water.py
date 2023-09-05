class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        The logic is to use two pointers and keep calculating the water contained between two lines.
        If height[i] < height[j], then first calculate the contained water using the smaller value among two and multiply
        it with their indexes difference. Then increment i with 1 because height[i] was smaller and moving to right could
        yield in greater contained water.
        If height[i] >= height[j], then first calculate the contained water using the smaller value among two and multiply
        it with their indexes difference. Then decrement j with 1 because height[j] was less than or smaller and moving
        to left could yield in greater contained water.
        """
        i, j = 0, len(height)-1
        max_water = 0
        while i != j:  # breaking condition is when both i & j are pointing to the same index
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