# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The idea is to store nodes of linked list 1 in array t1 and nodes of linked list 2 in array t2.
        Then we need to reverse t1 and t2. After reversing, we need to find if t1 and t2 length are equal. If the length is
        not equal then we need to prepend 0s to the shorter list to make the lengths equal. Now, we just need to iterate
        from right->left on any of the array i.e. t1 or t2 and find the digit sum for every iteration and keep on linking
        the nodes from head to tail.
        """
        t1 = []
        l1_length = 0
        t2 = []
        l2_length = 0
        carry = 0  # this will carry the carry if sum > 9
        head = None

        tempHead = l1
        while tempHead:  # prepare t1
            l1_length += 1
            t1.append(tempHead)
            tempHead = tempHead.next

        i, j = 0, l1_length - 1
        while i < j:  # reverse elements in t1
            temp = t1[j]
            t1[j] = t1[i]
            t1[i] = temp
            i += 1
            j -= 1

        tempHead = l2
        while tempHead:  # prepare t2
            l2_length += 1
            t2.append(tempHead)
            tempHead = tempHead.next

        i, j = 0, l2_length - 1
        while i < j:  # reverse elements in t2
            temp = t2[j]
            t2[j] = t2[i]
            t2[i] = temp
            i += 1
            j -= 1

        # If lengths are not equal then prepend 0s to the shorter list to make lengths equal
        if l1_length != l2_length:
            if l1_length > l2_length:  # if l1 length > l2 length then prepend 0s to t2 array
                temp = [0] * (l1_length - l2_length)
                t2 = temp + t2
            else:  # else prepend 0s to t1 array
                temp = [0] * (l2_length - l1_length)
                t1 = temp + t1

        # Now, iterate from right to left, find the sum and link the nodes
        for i in range(len(t1) - 1, -1, -1):
            val1 = 0 if t1[i] == 0 else t1[i].val
            val2 = 0 if t2[i] == 0 else t2[i].val
            sum = val1 + val2 + carry
            unit_digit = sum % 10  # for unit digit do "% 10"
            carry = sum // 10  # to find carry do "// 10"

            if i == len(t1) - 1:
                head = ListNode(val=unit_digit)  # this will be the head
                tempHead = head
            else:
                node = ListNode(val=unit_digit)
                tempHead.next = node
                tempHead = node

        if carry > 0:  # If carry is > 0 then link one more node with value as the carry
            tempHead.next = ListNode(val=carry)

        return head
