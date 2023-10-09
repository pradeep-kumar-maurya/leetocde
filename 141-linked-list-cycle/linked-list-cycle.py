# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        The idea is to store all the memroy id of the nodes in a set and if there is any cycle then
        the memory id of a particular node will definitely be in the set. If it's in set return True
        else retrun False after the while loop completes.
        """
        id_set = set()  # set to store node memory id

        # Iterate till the tail
        while head is not None:

            if id(head) in id_set:  # if node id found in the set then return True
                return True

            else:  # else add that node id in the set
                id_set.add(id(head))

            head = head.next  # move to next node

        return False
