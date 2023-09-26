class Solution:
    """
    The idea is to reverse the complete array first.
    Then reverse the subarray from index 0 -> k-1
    Then reverse the subarray from index k -> len(nums)-1
    """
    def swap(self, nums, i, j):
        while i < j:
            temp = nums[j]
            nums[j] = nums[i]
            nums[i] = temp
            i += 1
            j -= 1

    def rotate(self, nums, k):
        k = k % len(nums)  # for larger values of k, modulo (%) will bring down the k value
        if k == 0:
            return
        self.swap(nums, 0, len(nums)-1)
        self.swap(nums, 0, k-1)
        self.swap(nums, k, len(nums)-1)
