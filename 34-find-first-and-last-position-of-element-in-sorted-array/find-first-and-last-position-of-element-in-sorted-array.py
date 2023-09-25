class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        is_break = False
        index = -1
        left_most_index = -1
        right_most_index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                left_most_index = mid
                right_most_index = mid
                is_break = True
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        if is_break is False:
            return [-1, -1]

        left, right = 0, index-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_most_index = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        left, right = index + 1, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right_most_index = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return [left_most_index, right_most_index]
