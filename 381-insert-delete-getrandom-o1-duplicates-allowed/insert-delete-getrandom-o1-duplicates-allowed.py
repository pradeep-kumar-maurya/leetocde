class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:  # this is O(1)
        self.values.append(val)
        if self.map.get(val) is None:
            self.map[val] = {len(self.values) - 1}
            return True
        else:
            self.map[val].add(len(self.values) - 1)
            return False

    def remove(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:
            index1 = next(iter(self.map.get(val)))
            if index1 == len(self.values) - 1:
                self.values.pop()
                self.map[val].remove(index1)
                if len(self.map[val]) == 0:
                    self.map.pop(val)
            else:
                self.values[index1] = self.values[-1]
                self.values[-1] = val
                self.map[self.values[index1]].remove(len(self.values) - 1)
                self.map[self.values[index1]].add(index1)
                self.values.pop()
                if self.values[index1] != val:
                    self.map[val].remove(index1)
                if len(self.map[val]) == 0:
                    self.map.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.values)  # this is O(1)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()