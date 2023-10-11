# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = head
        linked_list_length = 0

        while tempHead:
            linked_list_length += 1
            tempHead = tempHead.next

        nth_node_to_delete = linked_list_length - n + 1
        tempHead = head
        count = 0
        dummy_node = head

        while tempHead:
            count += 1
            if count == nth_node_to_delete:
                if count == 1:
                    head = head.next
                else:
                    dummy_node.next = tempHead.next
            dummy_node = tempHead
            tempHead = tempHead.next

        return head
