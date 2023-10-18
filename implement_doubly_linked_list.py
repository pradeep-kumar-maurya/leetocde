class DoublyLinkedList:
    def __init__(self, val=0):
        # Doubly linked list node will have 3 data i.e. link to previous node, value of the node and link to next node
        self.prev = None  # points to previous node
        self.val = val  # value of the node
        self.next = None  # points to next node

    # below method will add nodes to the right of the given node
    def add_node_to_right(self, leftNode, rightNode):  # here rightNode has to be added to the right of leftNode
        nextNode = leftNode.next
        if nextNode:  # if leftNode.next is not None then we need to point next of rightNode to nextNode
            rightNode.next = nextNode
            nextNode.prev = rightNode  # nextNode prev must point to rightNode
        leftNode.next = rightNode  # now leftNode.next should point to rightNode
        rightNode.prev = leftNode  # and rightNode.prev should point to leftNode
        if nextNode is None:  # if nextNode is None then rightNode will be the new tail therefore return it
            return rightNode

    # below method will add nodes to the left of the given node
    def add_node_to_left(self, leftNode, rightNode):
        prevNode = rightNode.prev
        if prevNode:  # if rightNode.prev is not None then we need to point next of prevNode to leftNode
            prevNode.next = leftNode
            leftNode.prev = prevNode  # leftNode.prev must point to prevNode
        leftNode.next = rightNode  # now leftNode.next must point to rightNode
        rightNode.prev = leftNode  # and rightNode.prev must point to leftNode
        if prevNode is None:  # if prevNode is None then leftNode will be the new head therefore return it
            return leftNode


d1 = DoublyLinkedList(10)
head = tail = d1

d2 = DoublyLinkedList(20)
node = d2.add_node_to_right(rightNode=d2, leftNode=d1)
if node is not None:
    tail = node

d3 = DoublyLinkedList(30)
node = d3.add_node_to_right(rightNode=d3, leftNode=d2)
if node is not None:
    tail = node

d4 = DoublyLinkedList(40)
node = d4.add_node_to_left(leftNode=d4, rightNode=d1)
if node is not None:  # if something is returned that means it will be the new head
    head = node

d5 = DoublyLinkedList(50)
node = d5.add_node_to_left(leftNode=d5, rightNode=d2)
if node is not None:
    head = node

while head:
    print(head.val, end=' ')
    head = head.next
print()
while tail:
    print(tail.val, end=' ')
    tail = tail.prev
