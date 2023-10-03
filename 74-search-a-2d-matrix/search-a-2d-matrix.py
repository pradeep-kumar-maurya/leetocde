class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        The idea is that the matrix rows are sorted and the first integer of each row is greater than the last integer of
        the previous row. Therefore, we will first apply binary search on the 1st column and then determine the only row we
        will be searching for the target element. Once we find the row then we will again apply binary search to find the
        target element. Overall T.C = O(log(m+n))
        """
        top, bottom = 0, len(matrix) - 1  # first binary search would be applied on the 1st column
        mid = 0
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] == target:  # if the 1st element of the row matches then return True directly
                return True
            elif matrix[mid][0] > target:  # if the mid is > target then decrement bottom
                bottom = mid - 1
            else:  # else increment mid
                top = mid + 1

        # After the first binary search, mid would be either pointing to the row next to the actual row or would be pointing
        # to the actual row. If the row pointed by mid have its first element > target then we will decrement mid by 1 which
        # will then point to the actual row where we need to apply the binary search to find the target element.
        if matrix[mid][0] > target:
            mid -= 1

        search_row = matrix[mid]  # we will save the actual row in a variable to apply the binary search
        left, right = 0, len(search_row) - 1
        while left <= right:
            mid = (left + right) // 2
            if search_row[mid] == target:  # if the element is found then return True else return False after the loop ends
                return True
            elif search_row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
