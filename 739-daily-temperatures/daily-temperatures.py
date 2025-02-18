class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        top = -1
        ans = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if top == -1:
                top += 1
                stack.append([temperatures[i], i])

            else:
                if temperatures[i] < stack[top][0]:
                    top += 1
                    stack.append([temperatures[i], i])
                else:
                    while top > -1 and temperatures[i] > stack[top][0]:
                        index = stack[top][1]
                        ans[index] = i - index
                        stack.pop(top)
                        top -= 1

                    top += 1
                    stack.append([temperatures[i], i])

        return ans
