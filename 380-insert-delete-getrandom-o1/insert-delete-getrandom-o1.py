class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:  # "is not None" is important because index 0 can cause "if" to fail
            return False
        else:
            self.values.append(val)
            self.map[val] = len(self.values) - 1
            return True

    def remove(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:  # "is not None" is important because index 0 can cause "if" to fail
            index = self.map.get(val)
            if index == len(self.values) - 1:
                self.values.pop()
                self.map.pop(val)
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