# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        The idea is to maintain a tail array that will contain the nodes that needs to be reversed. We are using tail array
        to optimize the T.C. We need to iterate over the tail array from right to left and consider two nodes at a time.
        We will also maintain two more nodes i.e. start_dummy_node which will be the node left to tails[0] and end_dummy_node
        which will be right to tails[-1].
        """
        tails = []  # array to contain the nodes that needs to be reversed
        count = 0
        tempHead = head
        start_dummy_node = None  # to maintain node that is left to tails[0]
        end_dummy_node = None  # to maintain node that is right to tails[-1]

        while tempHead:
            count += 1
            if count == left - 1:
                start_dummy_node = tempHead
            elif count == right + 1:
                end_dummy_node = tempHead
            if count >= left and count <= right:  # only append when count is >= left and <= right
                tails.append(tempHead)
            tempHead = tempHead.next

        if len(tails) == 1:  # if the length of tails array is 1 then simply return head
            return head

        # If the start_dummy_node is None that means left is 1, therefore, we need to also change the head to the last
        # node of the linked list
        newHead = None if start_dummy_node is None else head
        last_tail_index = len(tails) - 1
        second_last_tail_index = last_tail_index - 1

        while second_last_tail_index >= 0:
            last_tail = tails[last_tail_index]
            second_last_tail = tails[second_last_tail_index]

            # This "if" will only work if left is 1 because head will be changed by the last node of the linked list
            if newHead is None:
                newHead = last_tail  # last node will now be the new head
                newHead.next = head  # last node should now point to the original head
                second_last_tail.next = end_dummy_node  # 2nd last node should now point to end_dummy_node
                # start_dummy_node must be updated with the new head and this start_dummy_node will help us in inserting
                # upcoming nodes to their correct places
                start_dummy_node = newHead
            else:
                last_tail.next = start_dummy_node.next  # last node should point to start_dummy_node.next
                second_last_tail.next = end_dummy_node  # second_last_tail.next should point to end_dummy_node
                start_dummy_node.next = last_tail  # now start_dummy_node.next should point to the last node
                start_dummy_node = last_tail  # start_dummy_node must be updated to the last node

            last_tail_index -= 1  # decrement last_tail_index by 1 to get the new last node
            second_last_tail_index = last_tail_index - 1  # second_last_tail_index must be 1 less than last_tail_index

        return newHead
