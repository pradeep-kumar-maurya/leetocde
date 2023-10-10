# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        uniqueElements = set()
        tempSet = set()
        tempHead = head

        while tempHead:
            val = tempHead.val
            if val not in tempSet and val not in uniqueElements:
                uniqueElements.add(val)
            elif val not in tempSet and val in uniqueElements:
                tempSet.add(val)
                uniqueElements.remove(val)
            elif val in tempSet:
                pass
            tempHead = tempHead.next

        tempHead = head
        newHead = None
        second_node = None

        while tempHead:
            if tempHead.val in uniqueElements:
                if newHead is None:
                    second_node = tempHead
                    newHead = second_node
                    tempHead = tempHead.next
                else:
                    second_node.next = tempHead
                    second_node = second_node.next
                    tempHead = tempHead.next
            else:
                tempHead = tempHead.next

        if second_node:
            second_node.next = None
        return newHead
