class RandomizedSet:

    def __init__(self):
        self.map = set()

    def insert(self, val: int) -> bool:  # this is O(1)
        if val in self.map:
            return False
        else:
            self.map.add(val)
            return True

    def remove(self, val: int) -> bool:  # this is O(1)
        if val in self.map:
            self.map.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.map))  # this is O(N) because set is being converted to a list everytime
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()