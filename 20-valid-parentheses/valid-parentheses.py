class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = -1

        for char in s:
            if char in ("(", "[", "{"):
                top += 1
                stack.append(char)
            elif char == ")":
                if top >= 0 and stack[top] == "(":
                    stack.pop(top)
                    top -= 1
                else:
                    return False
            elif char == "]":
                if top >= 0 and stack[top] == "[":
                    stack.pop(top)
                    top -= 1
                else:
                    return False
            elif char == "}":
                if top >= 0 and stack[top] == "{":
                    stack.pop(top)
                    top -= 1
                else:
                    return False

        return True if top == -1 else False
