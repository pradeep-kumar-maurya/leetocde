class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The idea is to just find the two indexes i.e. i and j. These indexes will tell us about the first sorted subarray.
        If the array is completely sorted without any rotation then i = 0 and j = len(nums)-1
        If there are two sorted subarrays then i and j value changes as per the target value.
        """
        i, j = 0, len(nums)-1  # initially set i to 0 and j to len(nums)-1

        for k in range(1, len(nums), 1):
            if nums[k] < nums[k-1]:  # as soon if we find another sorted subarray then update j to k-1 and break
                j = k - 1
                break

        # If nums[0] > target then we need to search in the other sorted subaaray where left=j+1 & right=len(nums-1)
        if nums[0] > target:
            left, right = j+1, len(nums)-1
        else:  # else we need to search in the 1st sorted subarray where left=i and right=j
            left, right = i, j

        while left <= right:  # this is the binary search algorithm
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1  # return -1 if nothing returned from the while loop
