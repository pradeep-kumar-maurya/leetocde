class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        The idea is to create two hashmaps. 1st hashmap will store the frequency of characters from string s1 and is constant.
        2nd hashmap will be dynamic and will store the frequency of characters from string s2. As soon as the 1st hashmap is
        equal to the 2nd hashmap return True. If not till end, return False.
        """
        freq_dict_s1 = {}  # hashmap for s1
        freq_dict_s2 = {}  # hashmap for s2
        # This start index will be used to iterate over the string s2 from left to right and from a valid index i.e. index
        # from where we find a character in s2 that is present in s1. Also, while iterating we would decrement the frequencies
        # of the characters from 2nd hashmap.
        start_index = -1

        for char in s1:  # populate the 1st hashmap
            if freq_dict_s1.get(char) is None:
                freq_dict_s1[char] = 1
            else:
                freq_dict_s1[char] += 1

        for i, char in enumerate(s2):  # iterate over s2
            if freq_dict_s1.get(char):

                if start_index < 0:  # maintain the start_index
                    start_index = i

                if freq_dict_s2.get(char) is None:  # populate 2nd hashmap
                    freq_dict_s2[char] = 1
                else:
                    freq_dict_s2[char] += 1

                # Below "if" works if the frequency of character "char" in 2nd hashmap > 1st hashmap
                if freq_dict_s2[char] > freq_dict_s1[char]:
                    while True:  # While loop will break in between once start_index points to char in s2
                        if freq_dict_s2.get(s2[start_index]):
                            freq_dict_s2[s2[start_index]] -= 1  # decrement the frequency
                            if freq_dict_s2[s2[start_index]] == 0:  # pop the character if frequency is 0
                                freq_dict_s2.pop(s2[start_index])
                        if s2[start_index] == char:  # Break once start_index points to char in s2
                            break
                        start_index += 1  # increment start_index by 1 so that we reach the char in s2
                    # Incrementing 1 more time will bring start_index to a valid index from where we can find a valid
                    # permutation of s1 in s2.
                    start_index += 1

                # If len of 1st and 2nd hashmaps are equal then check if the items matches
                if len(freq_dict_s2) == len(freq_dict_s1):
                    if freq_dict_s2 == freq_dict_s1:  # return True if both hashmaps are equal
                        return True
            # If there is a character which will not be a part of the permutation then set start_index to -1 and set the
            # 2nd hashmap to an empty hashmap.
            else:
                start_index = -1
                freq_dict_s2 = {}

        return False
