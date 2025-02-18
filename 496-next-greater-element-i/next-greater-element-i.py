class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        top = -1
        my_dict = {}
        ans = []

        for i in range(len(nums2)):
            if top == -1:
                top += 1
                stack.append(nums2[i])
            else:
                if nums2[i] < stack[top]:
                    stack.append(nums2[i])
                    top += 1
                else:
                    while top > -1 and nums2[i] > stack[top]:
                        my_dict[stack[top]] = nums2[i]
                        stack.pop(top)
                        top -= 1
                    top += 1
                    stack.append(nums2[i])

        for num in stack:
            my_dict[num] = -1

        for num in nums1:
            ans.append(my_dict[num])

        return ans
