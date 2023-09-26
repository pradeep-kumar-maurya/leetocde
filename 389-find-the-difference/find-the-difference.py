class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
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
            if dict_s.get(key) is None:
                return key
            elif dict_s.get(key) != dict_t.get(key):
                return key
