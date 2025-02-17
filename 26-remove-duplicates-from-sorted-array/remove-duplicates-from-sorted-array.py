class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        # Intutive approach
        index = 0

        # keep checking if A[index] == A[i]. If not incement index and set A[index] to A[i]
        for i in range(len(A)):
            if A[index] != A[i]:
                index += 1
                A[index] = A[i]

        return index + 1

        # Alternate approach
        '''
        idx = 1
        ele = A[0]

        for i in range(1, len(A), 1):

            if A[i] != ele:
                ele = A[i]
                A[idx] = ele
                idx += 1

        return idx
        '''

