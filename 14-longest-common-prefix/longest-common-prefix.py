class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = ""
        min_str_length = 201  # max length of str in strs is 200

        for str in strs:
            if len(str) < min_str_length:
                min_str = str  # longest common prefix length can't exceed the smallest str length in strs list
                min_str_length = len(str)

        for str in strs:
            count = 0
            for j in range(len(min_str)):  # we just need to iterate over smallest str again and again for every str
                if min_str[j] == str[j]:
                    count += 1
                else:
                    if count == 0:  # count 0 means no common prefix in the entire strs list
                        return ""
                    elif count < min_str_length:  # we have to always look for the smallest count
                        min_str_length = count
                    break

        return min_str[: min_str_length]
