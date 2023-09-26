class Solution:

    def swap(self, nums, i, j):
        while i < j:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j -= 1

    def rotate(self, nums, k):
        k = k % len(nums)
        if k == 0:
            return
        self.swap(nums, 0, len(nums)-1)
        self.swap(nums, 0, k-1)
        self.swap(nums, k, len(nums)-1)
