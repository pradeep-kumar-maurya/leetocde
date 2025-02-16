class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # we will use sum of nos from 0 to n. Then subtratc from sum of nos in nums. That will be the ans.
        total_sum = 0
        actual_sum = 0

        for i in range(len(nums) + 1):
            total_sum += i

        for num in nums:
            actual_sum += num

        return total_sum - actual_sum
