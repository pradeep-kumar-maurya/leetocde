class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        total_count = 0
        max_count = 0
        max_element_count = 0
        max_element = ""
        freq_map = {}
        i, j = 0, 0

        while j < len(s):  # AAAAABBBBCBB
            total_count += 1

            if freq_map.get(s[j]) is None:
                freq_map[s[j]] = 1
            else:
                freq_map[s[j]] += 1

            if freq_map[s[j]] >= max_element_count:
                max_element_count = freq_map[s[j]]
                max_element = s[j]

            if len(freq_map) > k + 1 or (total_count - max_element_count) > k:  # AAAAABBBBCBB
                while (total_count - max_element_count) > k:
                    total_count -= 1
                    if total_count > max_count:
                        max_count = total_count
                    freq_map[s[i]] -= 1
                    if freq_map.get(s[i]) == 0:
                        freq_map.pop(s[i])
                    if s[i] == max_element:
                        max_element_count -= 1
                        for key in freq_map.keys():
                            if freq_map.get(key) > max_element_count:
                                max_element_count = freq_map[key]
                                max_element = key
                    i += 1
            j += 1

        if total_count > max_count:
            max_count = total_count

        return max_count
