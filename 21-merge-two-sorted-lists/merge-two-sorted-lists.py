# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        The idea is to iterate over both the linked lists and compare node values and link the nodes to tempHead in
        ascending order. tempHead will store the overall merged linked list. head will store the head of the temphead
        which would be returned at the end.
        """
        head = None  # to store the head of the merged linked list
        tempHead = None  # to store the merge linked list

        # Iterate till one of them is None
        while list1 and list2:
            # if list1 value is <= list2 value
            if list1.val <= list2.val:
                if head is None:  # if head is None then create head
                    tempHead = list1
                    head = tempHead
                    list1 = list1.next  # move to the next node in list1
                else:  # else set tempHead.next
                    tempHead.next = list1
                    tempHead = tempHead.next  # set tempHead to tempHead.next
                    list1 = list1.next

            # else list2 value is < list1 value
            else:
                if head is None:  # if head is None then create head
                    tempHead = list2
                    head = tempHead
                    list2 = list2.next
                else:  # else set tempHead.next
                    tempHead.next = list2
                    tempHead = tempHead.next  # set tempHead to tempHead.next
                    list2 = list2.next

        # if list1 is over and list2 still have some values
        if list1 is None and list2 is not None:
            # then iterate over list2
            while list2:
                if head is None:
                    tempHead = list2
                    head = tempHead
                    list2 = list2.next
                else:
                    tempHead.next = list2
                    tempHead = tempHead.next
                    list2 = list2.next

        # if list2 is over and list1 still have some values
        elif list2 is None and list1 is not None:
            # then iterate over list1
            while list1:
                if head is None:
                    tempHead = list1
                    head = tempHead
                    list1 = list1.next
                else:
                    tempHead.next = list1
                    tempHead = tempHead.next
                    list1 = list1.next
        # at last return head
        return head
