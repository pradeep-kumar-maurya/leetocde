class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        The idea is to fetch the smallest string and then iterate over the characters of the smallest string and then
        compare the characters of all the strings in strs one by one. If we find any mismatch character then just break
        and return the ans.
        """
        smallest_string = ""
        smallest_string_length = 201  # max string length would be 200 therefore using 201
        i = 0
        ans = ""
        is_break = False
        for string in strs:  # fetch the smallest string and length of the smallest string
            if len(string) < smallest_string_length:
                smallest_string = string
                smallest_string_length = len(string)
        while i < len(smallest_string):  # iterate over the smallest string
            char = smallest_string[i]
            for string in strs:  # compare char with all the strings positioned at index 'i'
                if string[i] != char:
                    is_break = True
                    break  # if any string character is != char then just break
            if is_break:  # if break was there then break from while loop too
                break
            ans += char  # else keep on adding the char to ans
            i += 1  # keep on incrementing 'i'
            is_break = False  # change is_break to false after every for loop
        return ans
