class DoublyLinkedList:
    def __init__(self, key=0, val=0):
        self.prev = None
        self.val = (key, val)
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.left = None
        self.right = None

    def add(self, node: DoublyLinkedList):
        if self.right == node:
            return
        self.right.next = node
        node.prev = self.right
        self.right = node
        self.right.next = None

    def remove(self, node: DoublyLinkedList):
        leftNode = node.prev
        rightNode = node.next
        if self.right == node:
            return
        elif leftNode is None:
            self.left = rightNode
            self.left.prev = None
            return
        leftNode.next = rightNode
        rightNode.prev = leftNode

    def get(self, key: int) -> int:
        node = self.cache_dict.get(key)
        if node is None:
            return -1
        value = node.val[1]
        self.remove(node)
        self.add(node)
        return value

    def put(self, key: int, value: int) -> None:
        node = DoublyLinkedList(key, value)
        if self.left is None and self.right is None:
            self.left = node
            self.right = node
        else:
            self.add(node)
        if self.cache_dict.get(key):
            self.remove(self.cache_dict.get(key))
        self.cache_dict[key] = node
        if len(self.cache_dict) > self.capacity:
            self.cache_dict.pop(self.left.val[0])
            self.remove(self.left)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)