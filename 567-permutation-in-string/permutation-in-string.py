class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_dict_s1 = {}
        freq_dict_s2 = {}

        for char in s1:
            if freq_dict_s1.get(char) is None:
                freq_dict_s1[char] = 1
            else:
                freq_dict_s1[char] += 1

        start_index = -1
        for i, char in enumerate(s2):
            if freq_dict_s1.get(char):

                if start_index < 0:
                    start_index = i

                if freq_dict_s2.get(char) is None:
                    freq_dict_s2[char] = 1
                else:
                    freq_dict_s2[char] += 1

                if freq_dict_s2[char] > freq_dict_s1[char]:
                    while True:
                        if s2[start_index] != char:
                            if freq_dict_s2.get(s2[start_index]):
                                freq_dict_s2[s2[start_index]] -= 1
                                if freq_dict_s2[s2[start_index]] == 0:
                                    freq_dict_s2.pop(s2[start_index])
                        elif s2[start_index] == char:
                            if freq_dict_s2.get(s2[start_index]):
                                freq_dict_s2[s2[start_index]] -= 1
                                if freq_dict_s2[s2[start_index]] == 0:
                                    freq_dict_s2.pop(s2[start_index])
                            break
                        start_index += 1
                    start_index += 1

                if len(freq_dict_s2) == len(freq_dict_s1):
                    if freq_dict_s2 == freq_dict_s1:
                        return True
            else:
                start_index = -1
                freq_dict_s2 = {}

        return False
