# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        The idea is to first calculate the length of the linked list. And then find the value of k so that k is in range
        [0, len(linked list) - 1]. Now we need to bring last k nodes to the front and starting len(linked list) - 1 nodes
        to the last.
        """
        tempHead = head
        ll_length = 0

        # calculate the length of the linked list
        while tempHead:
            ll_length += 1
            tempHead = tempHead.next

        if ll_length == 0:  # if the length is 0 return head
            return head

        k = k % ll_length  # do the modulo with len(linked list) because k can be very large
        if k == 0:  # if k is 0 i.e. multiple of len(linked list) then return head because no rotations are needed
            return head

        stop = ll_length - k  # stop is nothing but the no. starting nodes that will move to the end
        tempHead = head
        count = 0  # this count will help us to break

        # Iterate over the nodes from head till stop
        while tempHead:
            count += 1
            if count == stop:  # if count == len(linked list) - k then break
                break
            tempHead = tempHead.next

        # After break, tempHead.next should be the newHead because all those nodes will come at the starting
        newHead = tempHead.next
        # Now set tempHead.next to None because current tempHead will be the last in the rotated linked list. This is very crucial
        tempHead.next = None
        # We will maintain 2nd last node i.e. node before None because 2nd last node should point to head of the original linked list
        # because in this way we will get our final rotated linked list. 2nd last node must be calculated from the newHead node that
        # was calculated from the above while loop after breaking.
        secondLastNode = None
        tempHead = newHead

        while tempHead:  # Iterate using the newHead
            secondLastNode = tempHead  # maintain the 2nd last node until tempHead is pointing to None
            tempHead = tempHead.next

        secondLastNode.next = head  # Now, just point 2nd last node to the head of the original linked list
        return newHead  # return the recently calculated newHead
