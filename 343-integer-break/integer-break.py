class Solution:
    def integerBreak(self, n: int) -> int:
        """
        The idea is to break 'n' in more than 1 part i.e. 2,3,4....n so that the sum of those parts are equal to 'n'.
        For eg: if 5 needs to broken in two parts/spaces then 1st part will be (5//2)+1 because 5 is an odd no. and we should add 1.
        Here 2 is the total no. of parts/empty spaces to fill. Now the 1st part will be 3.
        For 2nd part, we just have (5-3) left because we have already filled the 1st part with 3,therefore, we must reduce
        3 from n. Now we to fill 2 in 1 empty space, therefore, we need to do (2//1) which is 2.
        Now, the product will be 3 * 2 i.e. 6 if we break 5 into two parts.
        Similarly, we need to break 5 into 3, 4 and 5 parts and find the products of the parts and return the max product.
        """
        ans = 1
        k = 2  # constraint is to break n in >= k parts
        num = n

        # k will start from 2 and go till num i.e. n
        while k <= num:
            n = num  # for every iteration n must be set back to num
            # denominator will start from k and will go till 1. These are nothing but the parts the 'n' is broken into.
            denominator = k
            product = 1  # this will store the product of parts for every k or denominator
            # inner while loop will iterate only till denominator is > 1
            while denominator > 0:
                # odd
                if n % denominator:
                    temp = ((n // denominator) + 1)  # add 1 if n is odd
                    product = product * temp
                # even
                else:
                    temp = n // denominator
                    product = product * temp
                # decrease denominator by 1 every time because no. of empty parts/spaces will be reduced per iteration
                denominator -= 1
                # we need to reduce temp from n because as we fill the parts/spaces, overall n decreases
                n = n - temp
            if product > ans:
                ans = product
            k += 1  # increment k by 1 which is nothing but breaking n into more parts until k <= n

        return ans
