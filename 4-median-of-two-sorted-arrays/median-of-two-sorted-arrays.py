class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        The idea is to find only the left valid partition that means a partition which contains the elements that would
        appear at left in the overall sorted array. Then we can easily find the median because median would rather be only
        from the right partition or would be a combination of left and right partition based on the total no. of elements.
        Overall T.C = O(log(min(A, B)))
        """
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2  # 'half' will help in finding the index from array B to prepare the left partition

        # Swap A with B if len(A) > len(B) because we want to run binary search on the small array i.e. A
        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A)-1  # apply binary search on the smaller array i.e. A
        while True:
            # python can easily handle -ve division
            i = (l + r) // 2  # "i" is pointing to mid in array A
            j = half - i - 2  # "j" is pointing to an index in array B such that i + j = half. -2 is subtracted because we need index.

            # We will use "-infinity" and "infinity" is we go out of index in array A and B
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # This is the condition to check if the left partition is valid
            if Aleft <= Bright and Bleft <= Aright:
                # odd no. of total elements
                if total % 2:
                    # if total is odd then median will always lie in the right partition
                    return min(Aright, Bright)
                # even no. of total elements
                else:
                    # Aleft, Bleft are from left partition and Aright, Bright are from right partition
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # We need to reduce elements from A if the left partition is invalid
            elif Aleft > Bright:
                r = i - 1
            # We need to increase elements from A if the left partition is invalid
            else:
                l = i + 1
