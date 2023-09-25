class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums)-1
        while left >= 0 and right <= len(nums)-1:
            mid = (left + right) // 2
            if right == len(nums)-1 and left == len(nums)-1:
                if nums[mid] > nums[mid-1]:
                    return right
            elif left == 0 and right == 0:
                if nums[mid] > nums[mid+1]:
                    return left
            else:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid] < nums[mid+1]:
                    left = mid + 1
                elif nums[mid] < nums[mid-1]:
                    right = mid - 1