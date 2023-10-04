class Solution:
    def reverseWords(self, s: str) -> str:
        word_array = []
        string = ""

        for i in range(len(s)-1, -1, -1):
            if s[i] != " ":
                string += s[i]
            else:
                if string == "":
                    pass
                else:
                    word_array.append(string)
                    string = ""

        if string != "":
            word_array.append(string)

        for i, word in enumerate(word_array):
            string = ""
            j = len(word) - 1
            while j >= 0:
                string += word[j]
                j -= 1
            word_array[i] = string

        return " ".join(word_array)
