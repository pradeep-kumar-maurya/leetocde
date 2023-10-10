# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The idea is to first prepare a set that only has unique elements in it. Now iterate over the linked list and
        only consider the nodes that have their values in the unique element set. Smartly link the valid nodes and remove
        the duplicate nodes.
        """
        uniqueElements = set()  # set which will contain unique elements
        tempSet = set()  # set which will help in creating the uniqueElements set
        tempHead = head

        # Iterate over the linked list and create the uniqueElements set
        while tempHead:
            val = tempHead.val
            # condition to check the val is unique
            if val not in tempSet and val not in uniqueElements:
                uniqueElements.add(val)
            # if val in uniqueElements and not in tempSet then remove from uniqueElements and add to tempSet
            elif val not in tempSet and val in uniqueElements:
                tempSet.add(val)
                uniqueElements.remove(val)
            # if val already in tempSet then it's a duplicate and don't do anything
            elif val in tempSet:
                pass
            tempHead = tempHead.next

        tempHead = head
        newHead = None  # it will contain the head of the unique linked list
        secondNode = None  # secondNode will be used to link the unique nodes

        while tempHead:
            # if the node is in uniqueElements then consider the node
            if tempHead.val in uniqueElements:
                if newHead is None:  # if it's the first node then set newHead to node
                    secondNode = tempHead
                    newHead = secondNode
                    tempHead = tempHead.next
                else:  # else keep on linking nodes to secondNode and keep incrementing secondNode
                    secondNode.next = tempHead
                    secondNode = secondNode.next
                    tempHead = tempHead.next
            # else keep incrementing tempHead
            else:
                tempHead = tempHead.next

        if secondNode:  # if secondNode is not None then it will be the last node therefore point next to None
            secondNode.next = None
        return newHead
