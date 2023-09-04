class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict1, dict2 = {}, {}
        word = ""
        word_array = []
        index = 0
        for i in range(len(pattern)):
            if dict1.get(pattern[i]) is None:
                dict1[pattern[i]] = [i]
            else:
                dict1[pattern[i]].append(i)

        for i in range(len(s)):
            if s[i] != ' ':
                word += s[i]
            if s[i] == " " or i == len(s)-1:
                word_array.append(word)
                if dict2.get(word) is None:
                    dict2[word] = [index]
                else:
                    dict2[word].append(index)
                index += 1
                word = ""

        if len(dict1) != len(dict2):
            return False

        else:
            for i in range(len(pattern)):
                if dict1[pattern[i]] != dict2[word_array[i]]:
                    return False
            return True
