class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        freq_dict_t = {}
        for char in t:
            if freq_dict_t.get(char) is None:
                freq_dict_t[char] = 1
            else:
                freq_dict_t[char] += 1

        freq_dict_s = {}
        i, j = 0, 1
        min_length = len(s)
        min_indexes = None
        dummy_array = []
        index = 0
        ans = ""
        if freq_dict_t.get(s[0]):
            freq_dict_s[s[0]] = 1
            dummy_array.append([s[0], i])
            if len(freq_dict_s) == len(freq_dict_t) and freq_dict_s == freq_dict_t:
                min_indexes = [0, j-1]
        while j < len(s):
            if freq_dict_t.get(s[j]):
                data = freq_dict_s.get(s[j])
                if data is not None:
                    dummy_array.append([s[j], j])
                    freq_dict_s[s[j]] += 1
                    if data >= freq_dict_t.get(s[j]):
                        while True:
                            key = dummy_array[index][0]
                            if freq_dict_s.get(key)-1 >= freq_dict_t.get(key):
                                freq_dict_s[key] -= 1
                                index += 1
                            else:
                                break
                else:
                    freq_dict_s[s[j]] = 1
                    dummy_array.append([s[j], j])
                i = dummy_array[index][1]
                if len(freq_dict_s) == len(freq_dict_t):
                    check_min = True
                    for key in freq_dict_t.keys():
                        if freq_dict_s.get(key) < freq_dict_t.get(key):
                            check_min = False
                    if check_min:
                        if j-i+1 <= min_length:
                            min_length = j-i+1
                            min_indexes = [i, j]
            j += 1
        if min_indexes is not None:
            for i in range(min_indexes[0], min_indexes[1]+1, 1):
                ans += s[i]
        return ans
