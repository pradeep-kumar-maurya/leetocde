class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        The idea is to iterate over the bits i.e. 32 bits.
        We will iterate over the nums array and check if the ith bit of num is set. If yes, then we will maintain a
        variable that will count the no. of set bits found at the ith position. We then just need to take the modulo of
        the total set bits with 3 because every number appears thrice except one therefore if we count set bits at ith
        position then for the repeating nos. in nums array the count will be a multiple of 3. And if the set bit count at
        the ith position is not a multiple of 3 then we know that it's the extra bit from the non-repeating no.
        """
        ans = 0
        for i in range(0, 32, 1):
            set_bit_count = 0
            for num in nums:
                if (1 << i) & num > 0:  # checks if the ith bit is set
                    set_bit_count += 1  # add all the set bits present at the ith position
            if i == 31 and set_bit_count > 0:  # if a no. is -ve then while adding to ans variable use -2**i
                ans += ((-2 ** i) * (set_bit_count % 3))
            else:  # else use 2**i
                ans += ((2 ** i) * (set_bit_count % 3))
        return ans
