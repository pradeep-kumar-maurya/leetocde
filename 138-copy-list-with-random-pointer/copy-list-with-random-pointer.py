"""
# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tempHead = head
        deepcopyNodeDict = {}
        newHead = None
        tempNode = None

        while tempHead:
            node = Node(x=tempHead.val, next=tempHead.next, random=tempHead.random)
            deepcopyNodeDict[tempHead] = node
            if newHead is None:
                newHead = node
                tempNode = newHead
            else:
                tempNode.next = node
                tempNode = tempNode.next
            tempHead = tempHead.next

        tempHead = newHead

        while tempHead:
            data = deepcopyNodeDict.get(tempHead.random)
            tempHead.random = data
            tempHead = tempHead.next

        return newHead
