class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0

        while (n // 5) > 0:
            trailing_zeroes += n // 5
            n = n // 5

        return trailing_zeroes
