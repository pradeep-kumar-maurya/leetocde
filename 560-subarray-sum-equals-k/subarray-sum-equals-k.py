class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq_dict = {0: 1}  # dict to maintain freq of prefix sums
        prefix_sum = 0
        count = 0

        for num in nums:
            prefix_sum += num

            # 1st -> check if we can remove any subarray from back so that we get sum = k
            difference = prefix_sum - k
            if freq_dict.get(difference):
                count += freq_dict.get(difference)

            # 2nd -> if prefix sum is there or not in the freq_dict, just insert/update the value
            if freq_dict.get(prefix_sum):
                freq_dict[prefix_sum] += 1
            else:
                freq_dict[prefix_sum] = 1

        return count
