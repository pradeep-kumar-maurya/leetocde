class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_dict = {}
        for i in range(len(nums)):
            freq_dict[nums[i]] = i
        for i in range(len(nums)):
            j = freq_dict.get(target - nums[i])
            if j and j > i:
                return [i, j]
