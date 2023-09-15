class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        The idea here is to just use a set and iterate over the set using a for loop and then find the consecutive
        elements using a while loop inside the for loop. The overall T.C is O(N)
        """
        num_set = set()
        max_count = 0
        for i in nums:  # create the set that would be iterated
            num_set.add(i)
        for i in num_set:  # we need to iterate over the set and not the array
            """
            If i-1 is already there in the set then we don't need to check for the consecutive elements because going
            further we would get a case where i-1 is not in the set and then our while loop will calculate all the
            consecutive elements. This steps brings down the T.C
            """
            if i-1 not in num_set:
                count = 1  # count will always start from 1
                while True:  # if i-1 is not there in the set then while loop calculates the executive elements
                    if i+1 in num_set:  # we need to check i+1 in the set
                        count += 1
                        i += 1
                    else:  # else break from the while loop
                        break
                max_count = max(count, max_count)  # calculate the max
        return max_count
