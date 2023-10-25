class RandomizedCollection:
    """
    The idea is to use a list and a hashmap so that the getRandom() on a list is O(1). Insertion in the list will
    always be O(1) because we insert at the end. But removal from a list could be O(N), but removal could be of O(1)
    if that element is sent to the last index, therefore, last index element and element to be removed will be
    swapped and then pop() will be used to remove the last element from the list. Now, in this question, we can have
    duplicates, therefore, the values of the key in the map would be a set because we would be adding and removing
    data when we remove an element.
    """
    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:  # this is O(1)
        self.values.append(val)  # append every value to the values list
        if self.map.get(val) is None:
            self.map[val] = {len(self.values) - 1}  # value of the keys will be a set
            return True
        else:
            self.map[val].add(len(self.values) - 1)  # add the index when the element is a duplicate
            return False

    def remove(self, val: int) -> bool:  # this is O(1)
        if self.map.get(val) is not None:
            # below code will give us the very first element of a set
            index = next(iter(self.map.get(val)))  # .get() on the map will always give us a set of indexes
            # if the index is the last index then just do pop on the values list and remove that index from the set
            # corresponding to the last element.
            if index == len(self.values) - 1:
                self.values.pop()  # pop the very last element from the values list
                self.map[val].remove(index)
                if len(self.map[val]) == 0:  # if len of the set becomes 0 then pop that key from the map
                    self.map.pop(val)
            # Else, we need to pick 1st element from the set of the element that needs to be removed and should be swapped
            # with the last index element. After swapping, we need to remove one index from the set of the element that
            # was supposed to be removed. Also, one index has to be removed from the set of the very last element and
            # then the removed element index must be added to the last element set because the values were swapped.
            else:
                self.values[index] = self.values[-1]
                self.values[-1] = val
                # As last element will be popped that means the last index must be removed from the set of the last
                # index element because the overall size of the values list will be reduced.
                self.map[self.values[index]].remove(len(self.values) - 1)
                # Once the elements are swapped, last index element would now appear at the index of the element that
                # has to be removed, therefore, we need to add that index to the set of the last index element.
                self.map[self.values[index]].add(index)
                self.values.pop()  # pop the very last element from the values list
                # Below is a special case when the element to be removed is the last element and it has duplicates too.
                # We won't further remove the index from the set if the value to be removed is equal to value of the
                # element at index 'index'.
                if self.values[index] != val:
                    self.map[val].remove(index)
                if len(self.map[val]) == 0:  # if len of the set becomes 0 then pop that key from the map
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