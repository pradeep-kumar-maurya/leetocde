class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):  # if len(s) is smaller than len(t) we can't find s in t
            return False

        i, j = 0, 0  # 'i' will iterate over 's' and 'j' will iterate over 't'
        while i < len(s) and j < len(t):  # if any of the pointer reaches the end then break
            if s[i] == t[j]:  # if s[i] == s[j] the increment i and decrement j
                i += 1
                j += 1
            else:  # else just increment j
                j += 1
        # If i == len(s) that means i iterated completely over the string s
        return True if i == len(s) else False
