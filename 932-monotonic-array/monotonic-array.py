class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        for i in range(1, len(nums), 1):
            if nums[i] >= nums[i - 1]:
                pass
            else:
                break
        else:
            return True

        for i in range(0, len(nums)-1, 1):
            if nums[i] >= nums[i + 1]:
                pass
            else:
                break
        else:
            return True

        return False
