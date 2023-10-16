# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        The idea is to reverse the nodes in the same way we have used to reverse the entire linked list. But this time we
        will keep a count check and reverse the nodes in a specific range. In order to do this question, first check
        reversing the entire linked list approach.
        """
        count = 0
        tempHead = head
        # This approach uses two nodes i.e. tempHead and nextNode to reverse the linked list
        nextNode = tempHead.next if tempHead.next else None
        if nextNode is None:  # If nextNode is None then return head
            return head
        leftDummyNode = None  # this node will be left to the leftmost node that needs to be reversed
        rightDummyNode = None  # this node will be right to the rightmost node that needs to be reversed
        lastDummyNode = None  # this node is the last reversed node and should point to the rightDummyNode
        prevNode = None  # this node will keep the track of last head node in the reversed portion
        midHead = None  # this will be the head of the reversed portion

        while nextNode:  # we will use nextNode to iterate
            count += 1
            if count == left - 1:  # once count == left-1 then leftDummyNode must be populated with tempHead
                leftDummyNode = tempHead
            elif count == right + 1:  # once count == right+1 then rightDummyNode must be populated with tempHead
                rightDummyNode = tempHead
            if count >= left and count <= right:  # this is the range in which the nodes have to be reversed
                if midHead is None:  # midHead will be the last node in the revered portion
                    midHead = tempHead
                    midHead.next = None  # set midHead next to None
                    prevNode = midHead
                    lastDummyNode = tempHead  # lastDummyNode will always be the first midHead
                else:
                    midHead = tempHead
                    midHead.next = prevNode
                    prevNode = midHead
            tempHead = nextNode
            nextNode = nextNode.next
            # If nextNode is None then tempHead is pointing to the last node of the linked list.
            # Therefore, we need to consider the last node as well.
            if nextNode is None:
                count += 1  # increment count
                if count == right + 1:  # if count == right+1 then set rightDummyNode to tempHead
                    rightDummyNode = tempHead
                # if count falls in the reversing range then tempHead will be the new midHead and midHead next must point
                # to prevNode
                elif count >= left and count <= right:
                    midHead = tempHead
                    midHead.next = prevNode
                    prevNode = midHead

        if leftDummyNode is None:  # if left leftDummyNode is None that means left was 1 and midHead will be the new head
            head = midHead
        else:  # else point leftDummyNode next to midHead
            leftDummyNode.next = midHead

        # If lastDummyNode is None that means right would be pointing to the last node of the linked list.
        # But if lastDummyNode is not None, then lastDummyNode next must point to rightDummyNode.
        if lastDummyNode:
            lastDummyNode.next = rightDummyNode

        return head
