class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        The idea is to use Binary Search because if len(nums)>1 then there will always exist a number that is strictly
        greater than its neighbour. Also, we are asked to return index of any such element therefore, it becomes easy to
        apply binary search rather than iterating over N elements. We will move our left & right index based on the
        neighbour's value. If nums[mid] < nums[mid+1] then set left to "mid+1". Else if nums[mid] < nums[mid-1] then set
        right to "mid-1".
        There is a special case where both left and right point to the same element and are on either the last index i.e.
        len(nums)-1 or at the first index i.e. 0. In that case, we just need to check either the left element or the right
        element based on the index we are at.
        """
        if len(nums) == 1:  # we need to return 0 if len(nums)==1
            return 0
        left, right = 0, len(nums)-1
        while left >= 0 and right <= len(nums)-1:
            mid = (left + right) // 2
            # both left and right points to the last index
            if right == len(nums)-1 and left == len(nums)-1:
                # Therefore, just check if nums[mid] > nums[mid-1] because nums[mid+1] is out of range
                if nums[mid] > nums[mid-1]:
                    return right
            # both left and right points to the first index
            elif left == 0 and right == 0:
                # Therefore, just check if nums[mid] > nums[mid+1] because nums[mid-1] is out of range
                if nums[mid] > nums[mid+1]:
                    return left
            else:
                # If we find any mid that satisfies all the conditions then just return the mid
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                # else increment left based on the values
                elif nums[mid] < nums[mid+1]:
                    left = mid + 1
                # or decrement right
                elif nums[mid] < nums[mid-1]:
                    right = mid - 1