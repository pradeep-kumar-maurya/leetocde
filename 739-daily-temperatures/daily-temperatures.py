class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        VVVVVVVImp:- Whenever we are asked about the next greatest element to a specific element in an array,
        we should always think of "stacks".
        '''
        stack = []
        top = -1
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if top == -1:
                top += 1
                stack.append([temperatures[i], i])

            else:
                # If array element is < stack top element, just add the element to the stack
                if temperatures[i] < stack[top][0]:
                    top += 1
                    stack.append([temperatures[i], i])
                else:
                    '''
                    Whenever the "array element" is > "stack top element", keep removing elements from the stack.
                    For all the removed elements from the stack, the "array element" will be its "next greatest element".
                    '''
                    while top > -1 and temperatures[i] > stack[top][0]:
                        '''
                        Add all the removed data from the stack to any data structure along with the array element
                        which was removing it. The data in the data structure gives us the info about array elements
                        and their corresponding next greatest elements.
                        '''
                        index = stack[top][1]
                        ans[index] = i - index
                        stack.pop(top)
                        top -= 1

                    # Now add that array element into the stack
                    top += 1
                    stack.append([temperatures[i], i])

        return ans
