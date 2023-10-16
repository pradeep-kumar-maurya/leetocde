# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 0
        tempHead = head
        nextNode = tempHead.next if tempHead.next else None
        if nextNode is None:
            return head
        leftDummyNode = None
        rightDummyNode = None
        lastDummyNode = None
        prevNode = None
        midHead = None

        while nextNode:
            count += 1
            if count == left - 1:
                leftDummyNode = tempHead
            elif count == right + 1:
                rightDummyNode = tempHead
            if count >= left and count <= right:
                if midHead is None:
                    midHead = tempHead
                    midHead.next = None
                    prevNode = midHead
                    lastDummyNode = tempHead
                else:
                    midHead = tempHead
                    midHead.next = prevNode
                    prevNode = midHead
            tempHead = nextNode
            nextNode = nextNode.next
            if nextNode is None:
                count += 1
                if count == right + 1:
                    rightDummyNode = tempHead
                elif count >= left and count <= right:
                    midHead = tempHead
                    midHead.next = prevNode
                    prevNode = midHead

        if leftDummyNode is None:
            head = midHead
        else:
            leftDummyNode.next = midHead

        if lastDummyNode:
            lastDummyNode.next = rightDummyNode

        return head
