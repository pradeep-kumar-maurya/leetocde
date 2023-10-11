# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        The idea is to find the nth node that has to be removed.
        This node can be calculated by (length of linked list - n + 1).
        """
        tempHead = head
        linked_list_length = 0

        while tempHead:
            linked_list_length += 1
            tempHead = tempHead.next

        nth_node_to_delete = linked_list_length - n + 1
        tempHead = head
        count = 0
        # We will maintain a dummy node which will be the left node to the deleting node and will point to the next node of
        # the deleting node.
        dummy_node = head

        while tempHead:
            count += 1
            if count == nth_node_to_delete:
                if count == 1:  # if count is 1 that means we need to delete the head therefore set head to head.next
                    head = head.next
                else:  # if count is > 1 then point dummy_node.next to tempHead.next
                    dummy_node.next = tempHead.next
            dummy_node = tempHead  # this dummy node should be 1 less than the tempHead node
            tempHead = tempHead.next

        return head
