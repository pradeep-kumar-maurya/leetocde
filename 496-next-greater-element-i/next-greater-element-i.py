class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        VVVVVVVImp:- Whenever we are asked about the next greatest element to a specific element in an array,
        we should always think of "stacks".
        '''
        stack = []
        top = -1
        my_dict = {}
        ans = []

        for i in range(len(nums2)):
            if top == -1:
                top += 1
                stack.append(nums2[i])
            else:
                # If array element is < stack top element, just add the element to the stack
                if nums2[i] < stack[top]:
                    stack.append(nums2[i])
                    top += 1
                else:
                    '''
                    Whenever the "array element" is > "stack top element", keep removing elements from the stack.
                    For all the removed elements from the stack, the "array element" will be its "next greatest element".
                    '''
                    while top > -1 and nums2[i] > stack[top]:
                        '''
                        Add all the removed data from the stack to any data structure along with the array element
                        which was removing it. The data in the data structure gives us the info about array elements
                        and their corresponding next greatest elements.
                        '''
                        my_dict[stack[top]] = nums2[i]
                        stack.pop(top)
                        top -= 1

                    # Now add that array element into the stack
                    top += 1
                    stack.append(nums2[i])

        # for left over data in the stack, just add it to the data structure with some default value
        for num in stack:
            my_dict[num] = -1

        for num in nums1:
            ans.append(my_dict[num])

        return ans
