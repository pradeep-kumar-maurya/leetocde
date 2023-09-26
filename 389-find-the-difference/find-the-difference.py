class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # The idea is to create two dictionaries and then compare the keys/values of the two dicts.
        dict_s = {}
        dict_t = {}

        for char in s:
            if dict_s.get(char) is None:
                dict_s[char] = 1
            else:
                dict_s[char] += 1

        for char in t:
            if dict_t.get(char) is None:
                dict_t[char] = 1
            else:
                dict_t[char] += 1

        for key in dict_t.keys():
            if dict_s.get(key) is None:  # If the key is not found in dict_s then key is the extra char
                return key
            elif dict_s.get(key) != dict_t.get(key):  # If the value of the key does not match then key is the extra char
                return key
