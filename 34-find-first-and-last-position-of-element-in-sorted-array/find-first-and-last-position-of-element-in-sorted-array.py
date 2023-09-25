class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        The idea is to first find the target element and its index. Then we will have two different while loops.
        1st while loop will only cover the left part of index. We will apply binary search to find the first target
        element from the left side.
        2nd while loop will only cover the right part of index. We will apply binary search to find the last target
        element from the right side.
        """
        left, right = 0, len(nums)-1
        is_break = False
        index = -1
        left_most_index = -1
        right_most_index = -1

        # This while loop fins the element and its index
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid  # this index will be used to distinguish left and right part for further binary searches
                left_most_index = mid  # we will set left most index to mid
                right_most_index = mid  # we will set right most index to mid too
                is_break = True  # this will help knowing if the target is present in nums or not
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # if is break is False that means the target was not present in the nums array
        if is_break is False:
            return [-1, -1]

        # This is the 1st while loop which find the first occurrence of the target element in nums array
        left, right = 0, index-1  # left will be 0 and right will start from index-1
        while left <= right:
            mid = (left + right) // 2
            # if found the target element in the left part then update left most index and set right to "mid-1"
            if nums[mid] == target:
                left_most_index = mid
                right = mid - 1
            # else set left to "mid+1"
            elif nums[mid] < target:
                left = mid + 1

        # This is the 2nd while loop which find the last occurrence of the target element in nums array
        left, right = index + 1, len(nums)-1  # left will be "index+1" and right will be len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            # if found the target element in the right part then update right most index and set left to "mid+1"
            if nums[mid] == target:
                right_most_index = mid
                left = mid + 1
            # else set right to "mid-1"
            elif nums[mid] > target:
                right = mid - 1

        return [left_most_index, right_most_index]
