class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = ""

        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                string += s[i]
            else:
                if string == "":
                    pass
                else:
                    return len(string)

        if string != "":
            return len(string)
