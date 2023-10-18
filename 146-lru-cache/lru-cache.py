"""
The idea is to use a hashmap and a doubly linked list so that the get and put operations are of O(1) average time.
The hashmap will store item as <key, value> where key is the provided key but value will be a node. Node value will
be a tuple i.e. (key, value). We are using node as the value of the key so that remove operation from the doubly linked
list will be of O(1).
"""

class DoublyLinkedList:
    def __init__(self, key=0, val=0):
        self.prev = None  # link to the previous node
        self.val = (key, val)  # value of the node is a tuple
        self.next = None  # link to the next node


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}  # this is the hashmap to store key and value pairs
        self.left = None  # this will point to the least recently used node
        self.right = None  # this will point to the most recently used node

    def add(self, node: DoublyLinkedList):
        if self.right == node:  # if right node is same as the provided node then just return
            return
        self.right.next = node  # else right node next should point to the provided node
        node.prev = self.right  # previous of provided node should point to right node
        self.right = node  # now update right node to provided node as it is the most recently added node
        self.right.next = None  # also, set right node next to None

    def remove(self, node: DoublyLinkedList):
        leftNode = node.prev  # node left to the provided node
        rightNode = node.next  # node right to the provided node
        if self.right == node:  # if the right most node == node then it should not be removed, therefore, just return
            return
        # if the leftNode of the provided node is None that means the provided node is the very left most node,therefore,
        # we just need to update left with rightNode and point previous of the new left node to None and return.
        elif leftNode is None:
            self.left = rightNode
            self.left.prev = None
            return
        # if none of the above condition is true then the provided node will be somewhere in between many nodes.
        # therefore, just point leftNode next to rightNode and rightNode previous to leftNode
        leftNode.next = rightNode
        rightNode.prev = leftNode

    def get(self, key: int) -> int:
        node = self.cache_dict.get(key)
        if node is None:  # if the key doesn't exist then return -1
            return -1
        value = node.val[1]  # else value will be node.val[1] because index 1 in the tuple stores the value of the key
        # now this node has to be removed and should be brought to the right most node in the doubly linked list
        # because it will be the most frequently used element
        self.remove(node)  # therefore, first remove the node from the list
        self.add(node)  # then add the same node to the right most position in the list
        return value  # and return the value

    def put(self, key: int, value: int) -> None:
        node = DoublyLinkedList(key, value)  # first create a node
        # If both left and right are None that means doubly linked list is empty, therefore, point left and right to node
        if self.left is None and self.right is None:
            self.left = node
            self.right = node
        else:  # else every node has to be added to the right of the right most node
            self.add(node)
        # If the key exits in the hashmap that means we need to update the value of the key. And just now we added this
        # new key-value pair node, therefore, first we need to remove the old node from the doubly linked list and then
        # update the key with the newly added node.
        if self.cache_dict.get(key):
            self.remove(self.cache_dict.get(key))
        # below code will either add a new pair or just update the existing key with a new node
        self.cache_dict[key] = node
        # if length of the cache dict is > capacity then we need to pop a pair from the dict and this popped pair should
        # be the least frequently used pair or the key. And left is always pointing to the least frequently used element
        # therefore, we also need to remove the left most node from the doubly linked list.
        if len(self.cache_dict) > self.capacity:
            self.cache_dict.pop(self.left.val[0])  # first remove the pair from the cache dict
            self.remove(self.left)  # then remove the node from the doubly linked list


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)