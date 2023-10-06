class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 1
        k = 2
        num = n

        while k <= num:
            n = num
            denominator = k
            product = 1
            while denominator > 0:
                if n % denominator:
                    temp = ((n // denominator) + 1)
                    product = product * ((n // denominator) + 1)
                else:
                    temp = n // denominator
                    product = product * (n // denominator)
                denominator -= 1
                n = n - temp
            if product > ans:
                ans = product
            k += 1

        return ans
