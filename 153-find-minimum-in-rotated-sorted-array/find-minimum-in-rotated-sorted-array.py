class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        The idea is to first find the mid and then compare the nums[mid] with nums[left] and nums[right].
        If we rotate array then the array is divided into two sorted subarrays i.e. left & right sorted subarrays.
        Now, every element in the right subarray will be less than the first element in the left subarray.
        If nums[mid] > nums[right], that means, doing a binary search in the right subarray will only give the
        smallest element because there is a subarray on the right side that is smaller than the left subarray.
        If nums[mid] < nums[left], that means, doing a binary search in the left subarray will only give the smallest
        element because every element in the right subarray is greater than nums[mid] and therefore, no smallest element
        lies there.
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            # If the smallest element lies at the last index then we compare it with nums[mid-1]
            if left == right == mid == len(nums)-1:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
            # This condition checks if the mid is pointing to the smallest element
            elif nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                return nums[mid]
            # If nums[mid] < nums[left], that means, the smallest element will be present in the left part
            elif nums[mid] < nums[left]:
                right = mid - 1
            # If nums[mid] > nums[right], that means, the smallest element will be present in the right part
            elif nums[mid] > nums[right]:
                left = mid + 1
            # This is a case where we encounter a subarray where all the elements are sorted in ascending order.
            # This means, nums[left] will be the smallest element in the subarray which would be the overall smallest element.
            elif nums[mid] > nums[left] and nums[mid] < nums[right]:
                return nums[left]
