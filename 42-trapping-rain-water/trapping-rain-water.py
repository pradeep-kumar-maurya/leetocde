class Solution:
    def trap(self, height: List[int]) -> int:
        max_height = 0
        max_height_index = -1
        left_max = 0
        right_max = 0
        total_water = 0
        for i in range(len(height)):
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i
        for i in range(0, max_height_index, 1):
            if height[i] > left_max:
                left_max = height[i]
            total_water += (left_max - height[i])
        for i in range(len(height)-1, max_height_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            total_water += (right_max - height[i])
        return total_water
