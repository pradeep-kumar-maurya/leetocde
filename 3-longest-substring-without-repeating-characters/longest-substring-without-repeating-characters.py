class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        freq_dict = {}

        # Solving using a hashmap
        for i, char in enumerate(s):
            data = freq_dict.get(char)
            if data is None:  # if the char is absent in hashmap then increment count by 1
                freq_dict[char] = i
                count += 1
                if count > max_count:
                    max_count = count
            else:
                main_index = data  # fetch the index and store in one variable
                index = data  # again save the same index in another variable
                """
                The idea is to remove the duplicate element from the hashmap and also any other element that appears
                before the duplicate element in the string 's', therefore, a while loop is used with 3 conditions i.e.
                index >= 0 because python follows -ve indexing too.
                freq_dict.get(s[index]) is not None because if the data is None then we don't need to iterate further.
                freq_dict.get(s[index]) <= main_index otherwise it can remove a valid substring element which we don't want.
                """
                while index >= 0 and freq_dict.get(s[index]) is not None and freq_dict.get(s[index]) <= main_index:
                    freq_dict.pop(s[index])  # pop the element
                    index -= 1  # decrease index by 1
                    count -= 1  # decrease count by 1
                freq_dict[char] = i  # after the while loop ends add char to hashmap with new index value i.e. 'i'
                count += 1  # increase count by 1
                if count > max_count:
                    max_count = count

        return max_count
