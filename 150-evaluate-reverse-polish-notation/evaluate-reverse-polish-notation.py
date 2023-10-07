class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        top = -1
        stack = []

        for i in tokens:
            if i in ("+", "-", "*", "/"):
                b = int(stack[top])
                a = int(stack[top - 1])
                if i == "+":
                    result = a + b
                elif i == "-":
                    result = a - b
                elif i == "*":
                    result = a * b
                else:
                    if (a / b) < 0:
                        result = str(a / b)
                        string = ""
                        for i in result:
                            if i == ".":
                                break
                            else:
                                string += i
                        result = -int(string[1:])
                    else:
                        result = a // b

                stack.pop(top)
                top -= 1
                stack.pop(top)
                stack.append(result)
            else:
                top += 1
                stack.append(int(i))

        return int(stack[top])
