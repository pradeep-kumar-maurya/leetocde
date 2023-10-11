# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        tails = []
        count = 0
        tempHead = head
        start_dummy_node = None
        end_dummy_node = None

        while tempHead:
            count += 1
            if count == left - 1:
                start_dummy_node = tempHead
            elif count == right + 1:
                end_dummy_node = tempHead
            if count >= left and count <= right:
                tails.append(tempHead)
            tempHead = tempHead.next

        if len(tails) == 1:
            return head

        newHead = None if start_dummy_node is None else head
        last_tail_index = len(tails) - 1
        second_last_tail_index = last_tail_index - 1

        while second_last_tail_index >= 0:
            last_tail = tails[last_tail_index]
            second_last_tail = tails[second_last_tail_index]

            if newHead is None:
                newHead = last_tail
                newHead.next = head
                second_last_tail.next = end_dummy_node
                start_dummy_node = newHead
            else:
                last_tail.next = start_dummy_node.next
                second_last_tail.next = end_dummy_node
                start_dummy_node.next = last_tail
                start_dummy_node = last_tail

            last_tail_index -= 1
            second_last_tail_index = last_tail_index - 1

        return newHead
