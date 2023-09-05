class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i < j:
            if (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57) and\
                    (65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122 or 48 <= ord(s[j]) <= 57):
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                elif 65 <= ord(s[i]) <= 90:
                    if ord(s[i]) + 32 == ord(s[j]):
                        i += 1
                        j -= 1
                    else:
                        return False
                elif 65 <= ord(s[j]) <= 90:
                    if ord(s[j]) + 32 == ord(s[i]):
                        i += 1
                        j -= 1
                    else:
                        return False
                else:
                    return False
            if (65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57) is False:
                i += 1
            if (65 <= ord(s[j]) <= 90 or 97 <= ord(s[j]) <= 122 or 48 <= ord(s[j]) <= 57) is False:
                j -= 1
        return True
