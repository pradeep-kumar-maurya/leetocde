class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in range(len(s)):
            arr1[ord(s[i])-97] += 1
            arr2[ord(t[i])-97] += 1
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

