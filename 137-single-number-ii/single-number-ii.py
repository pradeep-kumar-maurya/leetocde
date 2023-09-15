class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, 32, 1):
            set_bit_count = 0
            for num in nums:
                if (1 << i) & num > 0:
                    set_bit_count += 1
            if i == 31 and set_bit_count > 0:
                ans += ((-2 ** i) * (set_bit_count % 3))
            else:
                ans += ((2 ** i) * (set_bit_count % 3))
        return ans
