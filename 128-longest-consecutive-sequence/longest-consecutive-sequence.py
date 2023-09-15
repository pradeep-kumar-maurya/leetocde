class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        max_count = 0
        for i in nums:
            num_set.add(i)
        for i in num_set:
            if i-1 not in num_set:
                count = 1
                while True:
                    if i+1 in num_set:
                        count += 1
                        i += 1
                    else:
                        break
                max_count = max(count, max_count)
        return max_count
