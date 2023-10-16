# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The idea is very simple. We need to take one node at a time like it's a new linked list. Then we keep on pointing
        the upcoming nodes to the separated out nodes. This way our linked list will be reversed.
        For eg:- 1->2->3. Now, we will take node 1 and point its next to None. Then we will take node 2 and point it to
        node 1 i.e. 2.next = node 1. Similarly, we will point node 3 to node 2 i.e. 3.next = node 2. This will reverse the list.
        T.C = O(N) and S.C = O(N)
        """
        tempHead = head
        nextNode = tempHead.next if tempHead is not None else None  # this node will help in iterating the linked list
        newHead = head
        prevNode = None  # this will help in pointing newHead to previous head

        # We will iterate over nextNode
        while nextNode:
            # If newHead is None then set newHead to tempHead. Set newHead.next to None as it will be the last Node when
            # reversed. Also, store newHead in prevNode.
            if newHead is None:
                newHead = tempHead
                newHead.next = None
                prevNode = newHead
            # else set newHead to tempHead. Then set newHead.next to prevNode and set prevNode to current newHead
            else:
                newHead = tempHead
                newHead.next = prevNode
                prevNode = newHead
            tempHead = nextNode  # set tempHead to nextNode
            nextNode = nextNode.next  # nextNode will always be the node right to tempHead
            # If nextNode.next is None then tempHead will point to the last node which is not included till now.
            # Therefore, newHead will now point to tempHead and newHead.next will point to prevNode.
            if nextNode is None:
                newHead = tempHead
                newHead.next = prevNode

        return newHead
