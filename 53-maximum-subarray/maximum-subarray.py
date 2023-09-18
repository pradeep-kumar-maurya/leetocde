class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        The idea is to use the sliding window technique here. If the window sum is < 0 then we won't count that window, and
        then we will set the sum variable to 0 and then start a new window. We will initially set sum variable based on the
        nums[0] value. If it's > 0 then sum = nums[0] else sum = 0. We will also set max to nums[0] and it will be updated
        going further.
        """
        sum = nums[0] if nums[0] > 0 else 0
        max = nums[0]

        for i in range(1, len(nums), 1):
            if nums[i] > max:  # set max to nums[i] if nums[i] > max. This will help in cases where there are only -ve intergers.
                max = nums[i]
            sum += nums[i]
            if sum < 0:  # is sum < 0 then make sum to 0
                sum = 0
            elif sum > 0:
                if sum > max:  # else if sum > max, then update max with sum as it's a sum elements of a window
                    max = sum
        return max

        