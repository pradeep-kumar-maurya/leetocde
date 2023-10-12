# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        t1 = []
        l1_length = 0
        t2 = []
        l2_length = 0
        carry = 0
        head = None

        tempHead = l1
        while tempHead:
            l1_length += 1
            t1.append(tempHead)
            tempHead = tempHead.next

        i, j = 0, l1_length - 1
        while i < j:
            temp = t1[j]
            t1[j] = t1[i]
            t1[i] = temp
            i += 1
            j -= 1

        tempHead = l2
        while tempHead:
            l2_length += 1
            t2.append(tempHead)
            tempHead = tempHead.next

        i, j = 0, l2_length - 1
        while i < j:
            temp = t2[j]
            t2[j] = t2[i]
            t2[i] = temp
            i += 1
            j -= 1

        if l1_length != l2_length:
            if l1_length > l2_length:
                temp = [0] * (l1_length - l2_length)
                t2 = temp + t2
            else:
                temp = [0] * (l2_length - l1_length)
                t1 = temp + t1

        for i in range(len(t1) - 1, -1, -1):
            val1 = 0 if t1[i] == 0 else t1[i].val
            val2 = 0 if t2[i] == 0 else t2[i].val
            sum = val1 + val2 + carry
            unit_digit = sum % 10
            carry = sum // 10

            if i == len(t1) - 1:
                head = ListNode(val=unit_digit)
                tempHead = head
            else:
                node = ListNode(val=unit_digit)
                tempHead.next = node
                tempHead = node

        if carry > 0:
            tempHead.next = ListNode(val=carry)

        return head
