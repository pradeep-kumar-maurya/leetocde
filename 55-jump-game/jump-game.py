class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        The idea is to first find the right most index i.e. 'last_index' where (i + nums[i] >= len(nums)-1) because the
        element at last_index will allow us to jump to the end of the array. Now our duty is to find indices from the
        left side of the last_index such that it allows us to reach till the last_index.
        Therefore, we need to iterate from right to left starting from the 'last_index' and whenever
        (i + nums[i] >= last_index) we just need to update 'last_index' with that 'i', because, index 'i' and element at
        index 'i' will contribute in reaching to the end of the array 'nums'.
        When we are at index 0 and (i + nums[i] >= last_index) then we return True i.e. we have found a way to reach to
        the end of the array 'nums' starting from index 0. Else, we return False.
        And, If the for loop ends without any return that means there is no way to reach to the end and therefore return False.
        Basically, we can say that we need to fina a flow from right to left such that we reach at index 0 and
        (i + nums[i] >= last_index) via which we can say that there's a way to reach the end of the array 'nums' starting
        from index 0.
        """
        if len(nums) == 1:
            return True
        last_index = -1  # set last_index to -1 because we consider +ve indexes
        # iterate from 2nd last index till 0 and find the last_index such that (i + nums[i] >= len(nums)-1)
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= len(nums)-1:
                last_index = i  # update last_index with 'i' and break
                break
        if last_index < 0:  # if last_index is < 0 that means there is no way to reach to the end
            return False
        for i in range(last_index, -1, -1):  # iterate from last_index till 0
            if i == 0 and i + nums[i] >= last_index:
                return True
            elif i == 0 and i + nums[i] < last_index:
                return False
            # keep on updating the last_index whenever (i + nums[i] >= last_index). Basically, last_index value will keep
            # on decreasing.
            if i + nums[i] >= last_index:
                last_index = i
        return False