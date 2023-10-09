# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0:
            return head

        tempHead = head
        ll_length = 0
        secondLastNode = None

        while tempHead:
            ll_length += 1
            tempHead = tempHead.next
        
        if ll_length == 0:
            return head

        k = k % ll_length
        if k == 0:
            return head

        stop = ll_length - k
        tempHead = head
        count = 0

        while tempHead:
            count += 1
            if count == stop:
                break
            tempHead = tempHead.next

        newHead = tempHead.next
        tempHead.next = None
        tempHead = newHead
        
        while tempHead:
            secondLastNode = tempHead
            tempHead = tempHead.next

        secondLastNode.next = head
        return newHead
