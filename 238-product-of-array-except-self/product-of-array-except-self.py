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

    """
    Below approach uses a prefix and a suffix multiplication array. S.C = O(N)
    def solve(nums):
        The idea is to use a prefix mul and a suffix mul array. This allows us to prepare the final array in O(N) T.C.
        But this approach uses O(N) extra space i.e. prefix and suffix mul arrays.
        prefix_mul = [0] * len(nums)
        prefix_mul[0] = nums[0]
        suffix_mul = [0] * len(nums)
        suffix_mul[-1] = nums[-1]
        ans_array = []

        for i in range(1, len(nums), 1):  # prepare prefix mul array
            prefix_mul[i] = prefix_mul[i-1] * nums[i]

        for i in range(len(nums)-2, -1, -1):  # prepare suffix mul array
            suffix_mul[i] = suffix_mul[i+1] * nums[i]

        for i in range(len(nums)):  #
            if i == 0:
                ans_array.append(suffix_mul[1])
            elif i == len(nums)-1:
                ans_array.append(prefix_mul[len(nums)-2])
            else:
                ans_array.append(prefix_mul[i-1] * suffix_mul[i+1])

        return ans_array

    """
