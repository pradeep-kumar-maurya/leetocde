class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mul = [0] * len(nums)
        prefix_mul[0] = nums[0]
        suffix_mul = [0] * len(nums)
        suffix_mul[-1] = nums[-1]
        ans_array = []

        for i in range(1, len(nums), 1):
            prefix_mul[i] = prefix_mul[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):
            suffix_mul[i] = suffix_mul[i+1] * nums[i]

        for i in range(len(nums)):
            if i == 0:
                ans_array.append(suffix_mul[1])
            elif i == len(nums)-1:
                ans_array.append(prefix_mul[len(nums)-2])
            else:
                ans_array.append(prefix_mul[i-1] * suffix_mul[i+1])

        return ans_array
