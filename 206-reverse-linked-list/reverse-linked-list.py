# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head

        temphead = head
        tails = []

        while temphead:
            tails.append(temphead)
            temphead = temphead.next

        last_tail_index = len(tails) - 1
        second_last_tail_index = last_tail_index - 1
        dummy_node = None
        newHead = None

        while head and head.next is not None:
            last_tail = tails[last_tail_index]
            second_last_tail = tails[second_last_tail_index]

            if newHead is None:
                newHead = last_tail
                newHead.next = head
                dummy_node = newHead
                second_last_tail.next = None

            else:
                second_last_tail.next = None
                last_tail.next = dummy_node.next
                dummy_node.next = last_tail
                dummy_node = last_tail

            last_tail_index -= 1
            second_last_tail_index = last_tail_index - 1

        return newHead
