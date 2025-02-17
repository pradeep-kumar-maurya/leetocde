class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        roman_to_integer_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0

        '''
        In roman nos, if a big no. is at the right of a small no. then we subtract small no. from big no.
        For eg:- IV, XL, XC, CD... etc.
        '''
        while i < len(s):

            if i == len(s) - 1:  # edge case if i is pointing to the last element
                num += roman_to_integer_dict[s[i]]
                i += 1

            elif roman_to_integer_dict[s[i]] >= roman_to_integer_dict[s[i + 1]]:
                num += roman_to_integer_dict[s[i]]
                i += 1
            else:
                temp_num_2 = roman_to_integer_dict[s[i + 1]]
                temp_num_1 = roman_to_integer_dict[s[i]]
                num += (temp_num_2 - temp_num_1)
                i += 2  # we need to jump by 2 whenever we subtract the integers

        return num