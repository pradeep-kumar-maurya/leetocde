class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        The idea is to create new nodes and link them in order as they are in the original list. Now in order to point
        random to the newly created nodes we will be needing a hashmap where the key will be a node from the original
        list and value will be the same node but newly created one.
        """
        tempHead = head
        deepcopyNodeDict = {}  # hashmap to store old and new nodes
        newHead = None  # this will store the head
        tempNode = None

        # below while loop will link the newly created nodes
        while tempHead:
            # we will create new nodes using the Node class
            node = Node(x=tempHead.val, next=tempHead.next, random=tempHead.random)
            # key will be the old node and value will be its new node
            deepcopyNodeDict[tempHead] = node
            if newHead is None:
                newHead = node
                tempNode = newHead
            else:
                tempNode.next = node
                tempNode = tempNode.next
            tempHead = tempHead.next

        tempHead = newHead

        # below while loop will make random to point to the newly created nodes instead of the old ones
        while tempHead:
            data = deepcopyNodeDict.get(tempHead.random)
            tempHead.random = data
            tempHead = tempHead.next

        return newHead
