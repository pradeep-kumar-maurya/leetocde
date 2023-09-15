class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        consecutive_nums = set()
        max_count = 0
        for i in nums:
            num_set.add(i)
        for i in nums:
            if i not in consecutive_nums:
                consecutive_nums.add(i)
                count = 1
                num = i
                while True:
                    if i+1 in num_set:
                        consecutive_nums.add(i+1)
                        count += 1
                        i += 1
                    else:
                        break
                while True:
                    if num-1 in num_set:
                        consecutive_nums.add(num-1)
                        count += 1
                        num -= 1
                    else:
                        break
                max_count = max(count, max_count)
        return max_count
