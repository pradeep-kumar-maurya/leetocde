class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        The idea is to fix one number and then use two pointers approach on the right side of the sorted array.
        T.C = O(NlogN + N^2) ~= O(N^2)
        """
        nums.sort()  # Array needs to be sorted. T.C = O(NlogN)
        freq_set = set()  # this will keep track of the nos that are already considered as the first element
        final_set = set()  # this will maintain only unique triplets

        for i in range(0, len(nums)-2, 1):  # O(N)
            if nums[i] not in freq_set:
                freq_set.add(nums[i])
            else:  # nums[i] already in freq_set then skip nums[i]
                continue
            sum = 0 - nums[i]
            j, k = i+1, len(nums)-1  # these are the two pointers
            while j < k:  # O(N)
                if nums[j] + nums[k] == sum:
                    final_set.add(tuple([nums[i], nums[j], nums[k]]))
                    j += 1
                    k -= 1
                elif nums[j] + nums[k] > sum:
                    k -= 1
                else:
                    j += 1
        return list(final_set)
