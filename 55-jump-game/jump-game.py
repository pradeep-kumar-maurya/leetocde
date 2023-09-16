class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        index = -1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= len(nums)-1:
                index = i
                break
        if index < 0:
            return False
        for i in range(index, -1, -1):
            if i == 0 and i + nums[i] >= index:
                return True
            elif i == 0 and i + nums[i] < index:
                return False
            if i + nums[i] >= index:
                index = i
        return False
