class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        temp = 1
        for i in range(0, len(nums)-1, 1):
            temp = temp * nums[i]
            ans[i+1] = temp
        temp = 1
        for i in range(len(nums)-1, 0, -1):
            temp = temp * nums[i]
            ans[i-1] = ans[i-1] * temp
        return ans
