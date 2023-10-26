class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        The idea is to iterate over the string s using sliding window and keep the frequency of characters in a hashmap.
        We will always maintain total_count which is the total no. of elements in a window and a max_element_count which tells us
        about the frequency of the element which appeared the most in the window. Also, we will maintain max_element which
        will be the character that appeared the most in a window. Also, there is some mathematics used to know once we cross k.
        """
        total_count = 0  # stores the count of chars in a window
        max_count = 0  # stores the final answer i.e. length of the longest substring containing the same letter
        max_element_count = 0  # frequency of the char that appeared most in the window.
        max_element = ""  # stores the char that appeared the most in a window
        freq_map = {}  # stores the frequency of chars in a window
        i, j = 0, 0  # 'i' is the left pointer of the window and 'j' is the right pointer of the window

        while j < len(s):  # 'j' will be used to iterate over the string s
            total_count += 1

            if freq_map.get(s[j]) is None:
                freq_map[s[j]] = 1
            else:
                freq_map[s[j]] += 1

            if freq_map[s[j]] >= max_element_count:
                max_element_count = freq_map[s[j]]  # frequency of the element that appeared the most in a window
                max_element = s[j]  # character that appeared the most in a window

            # We will either decrement the frequencies or pop an item from the hashmap if len of hashmap > (k + 1) or
            # (total_count - max_element_count) > k because this tells us that there are excess no. of different characters
            # than expected in a window/hashmap. If we subtract max_element_count from the total_count then this tells us
            # about the combined frequencies of the different characters in a window/hashmap. And if this difference is > k,
            # that means we have taken more no. of different characters to be replaced than k.
            if len(freq_map) > k + 1 or (total_count - max_element_count) > k:
                # Use a while loop because we need to decrement the frequencies until the window/hashmap has correct data
                while (total_count - max_element_count) > k:
                    # decrement total count by 1 because left pointer of the window i.e. 'i' will move in 1 step
                    total_count -= 1
                    if total_count > max_count:  # maintain the max_count
                        max_count = total_count
                    # decrement frequency of s[i] in the hashmap by 1 everytime because 'i' will move from left to right
                    # and while moving we will decrement the frequencies of s[i] in the hashmap
                    freq_map[s[i]] -= 1
                    if freq_map.get(s[i]) == 0:  # if frequency of any char is 0 then pop the character
                        freq_map.pop(s[i])
                    if s[i] == max_element:  # if s[i] is the max_element than max_element_count must be decremented by 1
                        max_element_count -= 1
                        # once max_element_count is decremented then we need to iterate over the hashmap and check if there
                        # is a char whose frequency is now greater than the max_element_count and is the maximum in the hashmap.
                        # If yes, the max_element_count must be updated with the new value i.e. max among the hashmap and
                        # also, max_element must be updated with the new char that has appeared the most in a window.
                        for key in freq_map.keys():
                            if freq_map.get(key) > max_element_count:
                                max_element_count = freq_map[key]
                                max_element = key
                    i += 1  # increment 'i' by 1 everytime
            j += 1  # increment 'j' by 1 everytime

        if total_count > max_count:  # last check to check if the max_count needs to be updated
            max_count = total_count

        return max_count
