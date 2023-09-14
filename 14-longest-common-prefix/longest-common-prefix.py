class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest_string = ""
        smallest_string_length = 201
        i = 0
        ans = ""
        is_break = False
        for string in strs:
            if len(string) < smallest_string_length:
                smallest_string = string
                smallest_string_length = len(string)
        while i < len(smallest_string):
            char = smallest_string[i]
            for string in strs:
                if string[i] != char:
                    is_break = True
                    break
            if is_break:
                break
            ans += char
            i += 1
            is_break = False
        return ans
