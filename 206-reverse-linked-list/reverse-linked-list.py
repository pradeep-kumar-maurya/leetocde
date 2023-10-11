# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        The idea is to create an array of all the nodes and then iterate over the node array from right to left and
        smartly link nodes from right to the starting and this way the linked list will be reversed.
        For eg:- 1->2->3->4. Now we will create an array of nodes i.e. [1, 2, 3, 4]. Now 4 should be moved to the starting,
        therefore, we will link 4 at the starting and 4.next will point to 1 and also 3.next should point to null. Now,
        linked list will look like 4->1->2->3. Now, we need to link 3.next to 1 and 4.next to 3 and point 2 to null. Linked
        list will look like 4->3->1->2. This just gives an idea on how to link nodes from right to the starting in order to
        reverse the list.
        """
        if head is None:
            return head
        if head.next is None:
            return head

        temphead = head
        tails = []  # this array will store all the nodes from the linked list

        while temphead:
            tails.append(temphead)
            temphead = temphead.next

        # We need to consider two nodes i.e. last and 2nd last node from tails array at a time
        last_tail_index = len(tails) - 1  # this is the last node of the linked list
        second_last_tail_index = last_tail_index - 1  # this is the 2nd last node of the linked list
        dummy_node = None  # dummy node will help in fitting node between two nodes when moving nodes from right to left
        newHead = None  # this will be the head of the reversed linked list

        # As we move nodes from right to left, slowly head node will come at the end and head.next will point to null.
        # Therefore, we are using head.next != None to check when to stop because at this point the linked list will be reversed.
        while head.next != None:
            # we will take two nodes at a time from the right side of the tails array
            last_tail = tails[last_tail_index]
            second_last_tail = tails[second_last_tail_index]

            if newHead is None:
                newHead = last_tail  # last tail will be the new head now
                newHead.next = head  # last tail should now point to the original head
                dummy_node = newHead  # this will point to the node that was recently added at the starting
                second_last_tail.next = None  # second last tail should point to null now

            else:
                second_last_tail.next = None  # second last node should always point to null
                # last node should point to dummy_node.next as it will sit between dummy_node and dummy_node.next
                last_tail.next = dummy_node.next
                # and dummy_node.next should point to last tail. This way last tail will sit in btw dummy_node and dummy_node.next
                dummy_node.next = last_tail
                dummy_node = last_tail  # dummy_node should now be updated with the last tail

            last_tail_index -= 1  # decrement last tail index with 1
            second_last_tail_index = last_tail_index - 1  # 2nd last tail should be 1 less than the last tail index

        return newHead
