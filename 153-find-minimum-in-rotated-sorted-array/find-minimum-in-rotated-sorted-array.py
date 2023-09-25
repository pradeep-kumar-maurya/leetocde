class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if left == right == len(nums)-1:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
            elif nums[mid-1] > nums[mid] and nums[mid+1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] > nums[left] and nums[mid] < nums[right]:
                return nums[left]
