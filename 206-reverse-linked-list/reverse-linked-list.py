# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None

        temp_head = head.next
        previous_node = head
        previous_node.next = None

        while temp_head is not None:
            dummy_head = temp_head
            temp_head = temp_head.next
            dummy_head.next = previous_node
            previous_node = dummy_head

        return previous_node

