class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_dict = {}
        for i, value in enumerate(nums):
            if freq_dict.get(value) is None:
                freq_dict[value] = [i]
            else:
                freq_dict[value].append(i)
        for i, value in enumerate(nums):
            element = target - value
            data = freq_dict.get(element)
            if data is not None and len(data) == 1 and data[0] > i:
                return [i, data[0]]
            elif data is not None and len(data) > 1:
                for j in data:
                    if j > i:
                        return [i, j]
