class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        The idea is, there can be max two nos. in the array that appears more than n/3 times.
        Therefore, we will use (ME1, freq1) and (ME2, freq2) to find the two Majority elements and at last we will count
        the frequency of ME1 and ME2 and if the frequency is > n/3 then we will conclude them in the answer array.
        """
        ME1, freq1 = None, 0
        ME2, freq2 = None, 0
        ans = []

        for i in nums:
            if i == ME1:  # is i == ME1 then increment freq1 by 1
                ME1 = i
                freq1 += 1
            elif i == ME2:  # if i == ME2 then increment freq2 by 1
                ME2 = i
                freq2 += 1
            elif ME1 is None:  # if ME1 is None after the above 2 conditions then first populate ME1 and increment freq1 by 1
                ME1 = i
                freq1 += 1
            elif ME2 is None:  # is ME2 is None after the above 3 conditions then populate ME2 and increment freq2 by 1
                ME2 = i
                freq2 += 1
            # if ME1 and ME2 both are not None then decrement freq1 and freq2 by 1
            elif ME1 is not None and ME2 is not None:
                freq1 -= 1
                freq2 -= 1
                if freq1 == 0:  # if freq1 is 0 then set ME1 to None
                    ME1 = None
                if freq2 == 0:  # if freq2 is 0 then set ME2 to None
                    ME2 = None

        # Now count the frequency of ME1 and ME2
        ME1_count, ME2_count = 0, 0
        for i in nums:
            if i == ME1:
                ME1_count += 1
            elif i == ME2:
                ME2_count += 1

        if ME1_count > (len(nums) // 3):  # if count of ME1 is > n/3 then append ME1 to ans array
            ans.append(ME1)
        if ME2_count > (len(nums) // 3):  # if count of ME2 is > n/3 then append ME2 to ans array
            ans.append(ME2)

        return ans
