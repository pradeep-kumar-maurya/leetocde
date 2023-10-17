# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        The idea is to keep on reversing nodes and whenever count == k then we need to maintain a secondLastNode and this
        secondLastNode next should point to the 1st node of the next reversed portion. We will also maintain a validLength
        and whenever we cross this validLength there will be no rotations and secondLastNode should point to lastRevNode
        which is nothing but the 1st node of the next linked list portion that has to be rotated.
        """
        if k == 1:  # if k == 1 then no rotations are required
            return head
        length = 0  # this will keep the length of the linked list
        tempHead = head
        while tempHead:
            length += 1
            tempHead = tempHead.next
        # validLength will help us in knowing when to stop further rotations
        validLength = length - (length % k)
        tempHead = head
        nextNode = tempHead.next  # we always need a nextNode for reversing the nodes
        prevNode = None  # this node will help us in adding nodes left to the rotated nodes
        count = 0  # this count will be used to reverse nodes in k groups
        tempCount = 0  # tempCount will keep a track of the overall count and tells when to stop further rotations
        newHead = None
        constHead = None  # this will be the overall head of the reversed linked list
        # lastRevNode node will be the very first node for every k group, we need to maintain this because after rotation
        # we need to point lastRevNode of every kth group to the node of the next kth+1 group
        lastRevNode = None
        # secondLastNode is very important as we will be updating lastRevNode for every kth group but kth-1 group should
        # point to the reversed kth group. secondLastNode will be updated when kth+1 group is reversed.
        secondLastNode = None

        while nextNode:
            count += 1
            tempCount += 1

            if newHead is None:
                newHead = tempHead
                prevNode = newHead
                # secondLastNode will always be 1 step behind the lastRevNode because kth-1 group has to link to kth group
                if tempCount == 1:
                    secondLastNode = newHead
                lastRevNode = newHead  # this will be updated for every kth group
            else:
                newHead = tempHead
                newHead.next = prevNode
                prevNode = newHead

            if count == k:  # once count == k, the magic starts
                if constHead is None:  # if constHead is None then set constHead to newHead
                    constHead = tempHead
                else:  # else secondLastNode next must point to the newHead of the recently reversed kth group
                    secondLastNode.next = newHead
                    secondLastNode = lastRevNode  # also, secondLastNode must be updated to lastRevNode for further processes
                count = 0  # set count to 0 as we will be reversing the next kth groups
                newHead = None  # newHead must be set to None for every kth group

            tempHead = nextNode
            nextNode = nextNode.next

            if nextNode is None:  # this means we have reached the last node of the list
                count += 1
                if count == k:
                    if constHead is None:  # if constHead is None then k must be equal to the length of the linked list
                        constHead = tempHead  # therefore constHead will be set to tempHead
                    # Below code will run for both i.e. if constHead is None or if constHead is not None
                    newHead = tempHead
                    newHead.next = prevNode
                    prevNode = newHead
                    secondLastNode.next = newHead  # previous kth node must point to tempHead now
                    lastRevNode.next = None
                else:  # if count != k then just set secondLastNode next to tempHead
                    secondLastNode.next = tempHead

            # If tempCount > validLength that means there will be no further rotations because we will never find another
            # kth group for rotation. Therefore, just set secondLastNode next to lastPrevNode and then break
            if tempCount > validLength:
                secondLastNode.next = lastRevNode
                break

        return constHead
