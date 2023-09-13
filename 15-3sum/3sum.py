class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        freq_dict = {}  # maintains numbers from nums array and their final index
        final_dict = {}

        for i in range(len(nums)):
            # we only maintain the last index of repeating number as it's enough to tell if a triplet can be formed
            freq_dict[nums[i]] = i

        for i in range(0, len(nums)-2, 1):  # 'i' is the first pointer
            for j in range(i+1, len(nums)-1, 1):  # 'j' is the 2nd pointer
                k = 0 - (nums[i] + nums[j])  # 'k' will be searched in the freq_dict
                """
                freq_dict.get(k) has to be > i and > j then only we would consider [nums[i], nums[j], k]
                as a valid triplet
                """
                if freq_dict.get(k) and freq_dict.get(k) > i and freq_dict.get(k) > j:
                    # we will sort the triplet and use it as a key to check for the repeated triplet in O(1) T.C
                    data = sorted([nums[i], nums[j], k])
                    if final_dict.get(tuple(data)) is None:
                        final_dict[tuple(data)] = data

        return final_dict.values()
