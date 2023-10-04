class Solution:
    def reverseWords(self, s: str) -> str:
        """
        The idea is to iterate over the string "s" from right to left and as soon as we find a word we will append that
        word in the word_array. Now, the word_array will contain words in reverse order therefore, we need to reverse them
        again and put them in the same array.
        NOTE: This can be solved in O(1) constant space if the string in python was mutable. The idea will be to use two
        pointers and reverse the complete string "s" in-place and later handle the leading or trailing spaces or multiple spaces.
        """
        word_array = []
        string = ""

        # Iterate over string "s" from right to left
        for i in range(len(s)-1, -1, -1):
            # Append s[i] to string variable if s[i] != " "
            if s[i] != " ":
                string += s[i]
            else:
                # Once s[i] == " " then check if string is equal to "". If yes, then there is no word to append in word_array
                if string == "":
                    pass
                # If string != "" that means there is a valid word that can be appended to word_array
                else:
                    word_array.append(string)
                    string = ""  # set string to "" once the word is appended

        # If string still contains some characters after the for loop ends then append it too in the word_array
        if string != "":
            word_array.append(string)

        # Now iterate over every word in the word_array and reverse it
        for i, word in enumerate(word_array):
            string = ""
            j = len(word) - 1
            while j >= 0:
                string += word[j]
                j -= 1
            word_array[i] = string

        return " ".join(word_array)
