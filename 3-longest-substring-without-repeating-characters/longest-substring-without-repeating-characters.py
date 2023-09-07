class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        count = 0
        freq_dict = {}

        for i, char in enumerate(s):  # bpfbhmipx
            data = freq_dict.get(char)
            if data is None:
                freq_dict[char] = i
                count += 1
                if count > max_count:
                    max_count = count
            else:
                main_index = data
                index = data
                while index >= 0 and freq_dict.get(s[index]) is not None and freq_dict.get(s[index]) <= main_index:
                    freq_dict.pop(s[index])
                    index -= 1
                    count -= 1
                freq_dict[char] = i
                count += 1
                if count > max_count:
                    max_count = count

        return max_count
