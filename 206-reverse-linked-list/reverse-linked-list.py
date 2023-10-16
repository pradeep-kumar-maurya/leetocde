# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempHead = head
        nextNode = tempHead.next if tempHead is not None else None
        newHead = head
        prevsNode = None

        while nextNode:
            if newHead is None:
                newHead = tempHead
                newHead.next = None
                prevsNode = newHead
            else:
                newHead = tempHead
                newHead.next = prevsNode
                prevsNode = newHead
            tempHead = nextNode
            nextNode = nextNode.next
            if nextNode is None:
                newHead = tempHead
                newHead.next = prevsNode

        return newHead
