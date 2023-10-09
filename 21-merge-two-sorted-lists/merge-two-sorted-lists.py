# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        tempHead = None

        while list1 and list2:

            if list1.val <= list2.val:
                if head is None:
                    tempHead = list1
                    head = tempHead
                    list1 = list1.next
                else:
                    tempHead.next = list1
                    tempHead = tempHead.next
                    list1 = list1.next

            else:
                if head is None:
                    tempHead = list2
                    head = tempHead
                    list2 = list2.next
                else:
                    tempHead.next = list2
                    tempHead = tempHead.next
                    list2 = list2.next

        if list1 is None and list2 is not None:
            while list2:
                if head is None:
                    tempHead = list2
                    head = tempHead
                    list2 = list2.next
                else:
                    tempHead.next = list2
                    tempHead = tempHead.next
                    list2 = list2.next

        elif list2 is None and list1 is not None:
            while list1:
                if head is None:
                    tempHead = list1
                    head = tempHead
                    list1 = list1.next
                else:
                    tempHead.next = list1
                    tempHead = tempHead.next
                    list1 = list1.next

        return head
