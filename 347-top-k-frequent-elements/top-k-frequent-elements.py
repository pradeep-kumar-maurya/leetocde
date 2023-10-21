class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = 0
        freq_dict = {}
        rev_dict = {}
        count = 0
        ans = []

        for num in nums:
            if freq_dict.get(num) is None:
                freq_dict[num] = 1
                temp_count = 1
            else:
                freq_dict[num] += 1
                temp_count = freq_dict[num]
            if temp_count > max_count:
                max_count = temp_count

        if len(freq_dict) == k:
            return freq_dict.keys()

        for key, val in freq_dict.items():
            if rev_dict.get(val) is None:
                rev_dict[val] = [key]
            else:
                rev_dict[val].append(key)

        while True:
            data = rev_dict.get(max_count)
            if data:
                ans.extend(data)
                count += len(data)
            if len(ans) == k:
                break
            max_count -= 1

        return ans
