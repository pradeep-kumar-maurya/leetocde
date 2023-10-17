# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head

        length = 0
        tempHead = head
        while tempHead:
            length += 1
            tempHead = tempHead.next

        validLength = length - (length % k)
        tempHead = head
        nextNode = tempHead.next
        prevNode = None
        count = 0
        tempCount = 0
        newHead = None
        constHead = None
        lastRevNode = None
        secondLastNode = None

        while nextNode:
            count += 1
            tempCount += 1

            if newHead is None:
                newHead = tempHead
                prevNode = newHead
                if tempCount == 1:
                    secondLastNode = newHead
                lastRevNode = newHead
            else:
                newHead = tempHead
                newHead.next = prevNode
                prevNode = newHead

            if count == k:
                if constHead is None:
                    constHead = tempHead
                else:
                    secondLastNode.next = newHead
                    secondLastNode = lastRevNode
                count = 0
                newHead = None

            tempHead = nextNode
            nextNode = nextNode.next

            if nextNode is None:
                count += 1
                if count == k:
                    if constHead is None:
                        constHead = tempHead
                    newHead = tempHead
                    newHead.next = prevNode
                    prevNode = newHead
                    secondLastNode.next = newHead
                    lastRevNode.next = None
                else:
                    if newHead is None:
                        secondLastNode.next = tempHead

            if tempCount > validLength:
                secondLastNode.next = lastRevNode
                break

        return constHead
