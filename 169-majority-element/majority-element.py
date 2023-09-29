class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        The idea is, we will iterate over the array and lets say element at index [i] is different than the element at index
        [i+1] then we can say that element at index [i+1] is reducing the frequency of the element at index [i].
        If element at index [i+1] = element at index [i], then it will increase the frequency of the element.
        This way all different elements will cancel each other frequencies and at last only 1 no. will be left with
        frequency > 0 i.e. the Majority Element.
        """
        ME = None  # Majority Element should be initially set to None
        freq = 0  # frequency should be 0 at the starting

        for i in nums:
            # If ME is None that means 'i' will be the ME. Also, if i == ME, then set ME to i and increment freq by 1
            if ME is None or i == ME:
                ME = i
                freq += 1
            # If i != ME that means, i will reduce the frequency of ME therefore decrement freq by 1
            elif i != ME:
                freq -= 1
                if freq == 0:  # if freq == 0 that means there is no ME therefore set ME back to None
                    ME = None

        return ME
