# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        node = head
        count = 0

        while node is not None:
            count += 1
            node = node.next

        upperbound = (count // 2) + 1
        i = 1

        while i < upperbound:
            temp_head = temp_head.next
            i += 1

        return temp_head
