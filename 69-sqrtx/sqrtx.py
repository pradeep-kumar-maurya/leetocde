class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1 or x == 2:
            return 1
        # Below for loop will only run for square root of n times
        for i in range(2, x, 1):
            if i * i == x:
                return i
            elif i * i > x:
                return i - 1
