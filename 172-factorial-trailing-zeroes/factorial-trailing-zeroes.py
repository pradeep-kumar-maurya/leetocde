class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        The idea is to just count the total no. of 5s that appears till n because 5 will always be a part of the
        multiplication where there is a trailing zero. Now, in order to check how many 5s are there we need to keep on
        dividing n by 5 until the division is > 0 and sum up all the quotients.
        """
        trailing_zeroes = 0

        # We keep on dividing n by 5 until the quotient is > 0
        while (n // 5) > 0:
            trailing_zeroes += n // 5  # sum all the quotients
            n = n // 5  # keep on dividing by 5 so it reaches till 0

        return trailing_zeroes
