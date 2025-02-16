class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_dict = {0: 1}
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            difference = prefix_sum - k
            if freq_dict.get(difference):
                count += freq_dict.get(difference)

            if freq_dict.get(prefix_sum):
                freq_dict[prefix_sum] += 1
            else:
                freq_dict[prefix_sum] = 1

        return count
