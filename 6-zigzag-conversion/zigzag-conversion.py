class Solution:
    def convert(self, s: str, n: int) -> str:
        
        result = ""  # will hold the final string
        k = 0  # this will maintain the current row no.
        toggle = 0  # this will help in incrementing the index based on the row no. k

        if n == 1:  # as it is string will be returned if n == 1
            return s

        while k < n:
            """
            -> temp is an array that will only hold only 2 data because we can move in two directions (think diagonally wise
            along with column wise) to find the next elements in the specific row i.e. top->down and down->top. The temp
            data are multiplied by 2 because we move in both the directions to find the next element.
            But first we move from top->down and then down->top.
            -> temp[0] = index to be added to 'i' to reach to the next element with (top->down and down->top) approach.
            -> temp[1] = index to be added to 'i' to reach to the next element with (down->top and top->down) approach.
            -> NOTE:- If we are at the 1st row then keep on adding temp[0] to 'i'. If we are at the last row then keep on
            adding temp[1] to 'i'.
            -> toggle has been added to find the next element in a row because we toggle the approaches. Therefore, if
            toggle=0 then temp[0] is added to 'i' else if toggle=1 then temp[1] is added to 'i'.
            -> Check by taking an example of an array like - [1, 2, 3, 4] which represent the row nos. Index start from 0.
            If we are at index 0 i.e. k=0 (row=1), then in order to come back to row 1 again, I need to first travel to
            right i.e. 1->2->3->4 (top->down) then travel to left again 4->3->2->1 (down-top) which is total of 6 traversals
            which is double of the elements right to index 0 and therefore we multiply the  data in temp array with 2.
            If we are at index 1 i.e. k=1 (row=2), then in order to come back to row 2 again, I need to first travel to
            right i.e. 2->3->4 (top->down) then travel to left again 4->3->2 (down->top) which is total of 4 traversals
            which is double of the elements right to index 0. But now, we need to move from left to right and then come
            back to row 2 again i.e. 2->1 (down->top) then 1>2 (top->down) which is total of 2 traversals which is double
            of the elements left to index 1. This will follow for all the next elements withing the specific row with toggling.
            """
            temp = [((n-1) - k) * 2, (k - 0) * 2]  # this is the formula to calculate the no. of indexes to skip
            i = k
            while i < len(s):
                result += s[i]
                if k == 0:  # only add temp[0] for 1st row
                    i += temp[0]
                elif k == n - 1:  # only add temp[1] for last row
                    i += temp[1]
                else:  # toggle the index increment based on the toggle value
                    i += temp[toggle]
                    toggle = toggle ^ 1  # XOR can toggle the value from 0>1 and 1>0
            k += 1  # increment the row no.
            toggle = 0  # always set toggle to 0 for the new rows

        return result