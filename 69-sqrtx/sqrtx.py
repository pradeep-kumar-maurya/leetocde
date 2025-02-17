class Solution:
    def mySqrt(self, x: int) -> int:
        # Keeping the upperbound of the for loop to max.
        # It won't matter because we return from the loop ASAP .
        for i in range(0, (2**31)-1, 1):
            if i ** 2 == x:
                return i
            elif i ** 2 > x:
                return i - 1

