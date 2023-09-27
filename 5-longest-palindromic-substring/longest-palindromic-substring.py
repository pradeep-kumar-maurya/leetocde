class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_length = 1
        index1, index2 = 0, 0
        for i in range(1, len(s)-1, 1):
            j = i - 1
            k = i + 1
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    length = k - j + 1
                    if length > max_length:
                        max_length = length
                        index1 = j
                        index2 = k
                else:
                    break
                j -= 1
                k += 1

        for i in range(0, len(s)-1, 1):
            if s[i] == s[i+1]:
                length = 2
                if length > max_length:
                    max_length = length
                    index1 = i
                    index2 = i + 1
                j = i - 1
                k = i + 2
                while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        length = k - j + 1
                        if length > max_length:
                            max_length = length
                            index1 = j
                            index2 = k
                    else:
                        break
                    j -= 1
                    k += 1

        return s[index1: index2+1]
