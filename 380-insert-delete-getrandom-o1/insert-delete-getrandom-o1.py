class RandomizedSet:
    """
    The idea is to use a list and a hashmap so that the getRandom() on a list is O(1). Insertion in the list will
    always be O(1) because we insert at the end. But removal from a list could be O(N), but removal could be of O(1)
    if that element is sent to the last index, therefore, last index element and element to be removed will be
    swapped and then pop() will be used to remove the last element from the list.
    """
    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:  # "is not None" is important because index 0 can cause "if" to fail
            return False
        else:
            self.values.append(val)
            self.map[val] = len(self.values) - 1  # appended value index will always be len(list) - 1
            return True

    def remove(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:  # "is not None" is important because index 0 can cause "if" to fail
            index = self.map.get(val)
            # If index of the removing element is the last index then just pop from list as well as hashmap
            if index == len(self.values) - 1:
                self.values.pop()
                self.map.pop(val)
            # Else, first swap the last element with the element to be removed and then pop it from the list as well as
            # hashmap. Also, change the index of the swapped element to the index of the removed element in the hashmap.
            else:
                self.values[index] = self.values[-1]
                self.values[-1] = val
                self.values.pop()
                self.map.pop(val)
                self.map[self.values[index]] = index
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.values)  # this is O(1)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()