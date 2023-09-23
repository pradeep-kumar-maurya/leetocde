class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        The idea is to first prepare "ans" array that only consists of prefix multiplications. The catch is, the prefix
        multiplication has to stored in the array at index "i+1". Therefore, 1st for loop will iterate from 0 -> len(nums)-1.
        To store the prefix and suffix multiplications we will use a temp array.
        Now, we need to calculate the suffix multiplications and put them in the "ans" array at position "i-1" by
        multiplying the suffix multiplications with ans[i-1]. Therefore, 2nd for loop will iterate from len(nums)-1 -> 1.
        This way we will have our final array.
        """
        ans = [0] * len(nums)  # first prepare 'ans' array
        ans[0] = 1  # set ans[0] to 1 because prefix muls will be placed at index "i+1"
        temp = 1  # this temp will store the multiplications
        for i in range(0, len(nums)-1, 1):  # for prefix muls iterate from 0 -> len(nums)-1
            temp = temp * nums[i]  # this is the prefix multiplication
            ans[i+1] = temp  # store prefix multiplication at index "i+1"
        temp = 1  # set temp to 1 again for the suffix multiplications
        for i in range(len(nums)-1, 0, -1):  # for suffix muls iterate from len(nums)-1 -> 1
            temp = temp * nums[i]  # this is the suffix multiplication
            # Store suffix multiplication at index "i-1" in the 'ans' array. Note that we multiply temp with ans[i-1]
            ans[i-1] = ans[i-1] * temp
        return ans
