class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        The idea is to just use a stack and keep on appending nos. to stack and as soon as we find any arithmetic operator
        then we need to do arithmetic operation between the first two nos. from the stack. Once done with the operation,
        we need to remove those two nos. and append answer in the stack.
        """
        top = -1
        stack = []

        for i in tokens:
            if i in ("+", "-", "*", "/"):
                b = int(stack[top])  # this is the top element i.e. right part to the operator
                a = int(stack[top - 1])  # this is the 2nd top element i.e. left part to the operator
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = a - b
                elif i == "*":
                    result = a * b
                else:
                    # division is a special case here because division between two integers always truncates toward zero
                    # if division is < 0 then do floor division and just consider the left part of the division i.e. part
                    # left to "."
                    if (a / b) < 0:
                        result = str(a / b)  # we convert floor division to a string to take the left part of "."
                        string = ""
                        for i in result:
                            if i == ".":  # if i == "." then break
                                break
                            else:  # else add i to string
                                string += i
                        result = int(string)
                    # if division > 0 then just do integer division
                    else:
                        result = a // b

                stack.pop(top)  # remove top as per the logic
                top -= 1  # decrement top by 1
                stack.pop(top)  # remove the 2nd top as per the logic
                stack.append(result)  # then append result to stack and result will be the top element
            else:
                top += 1
                stack.append(int(i))

        return int(stack[top])
