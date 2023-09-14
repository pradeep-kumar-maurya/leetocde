class Solution:
    def trap(self, height: List[int]) -> int:
        """
        The idea is that the water will be there only if the left and the right building are taller than the middle ones.
        Now, we must find the index of the max height building because we need to traverse from left->right and then
        right->left only till max height index.
        We will travel from left->right only till max height index and maintain the max height and keep on subtracting with
        height[i] and add it to the total water variable that is initially set to 0.
        In same way we travel from right->left only till max height index and maintain the max height and keep on
        subtracting with height[i] and add it to the total water variable.
        """
        max_height = 0
        max_height_index = -1
        left_max_height = 0  # this will maintain the max height while traversing from left->right
        right_max_height = 0  # this will maintain the max height while traversing from right->left
        total_water = 0
        for i in range(len(height)):  # iterate and find the max height index
            if height[i] > max_height:
                max_height = height[i]
                max_height_index = i
        for i in range(0, max_height_index, 1):  # iterate from left->right till max height index
            if height[i] > left_max_height:
                left_max_height = height[i]  # maintain the left max height
            total_water += (left_max_height - height[i])  # add the subtraction to total water
        for i in range(len(height)-1, max_height_index, -1):  # iterate from right->left till max height index
            if height[i] > right_max_height:
                right_max_height = height[i]  # maintain the right max height
            total_water += (right_max_height - height[i])  # add the subtraction to total water
        return total_water
