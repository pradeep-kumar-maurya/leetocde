class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        s_dict = {}
        s_list = s.split()

        if len(s_list) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern_dict.get(pattern[i]) is None:
                pattern_dict[pattern[i]] = s_list[i]
            else:
                if pattern_dict[pattern[i]] != s_list[i]:
                    return False

        for i in range(len(s_list)):
            if s_dict.get(s_list[i]) is None:
                s_dict[s_list[i]] = pattern[i]
            else:
                if s_dict[s_list[i]] != pattern[i]:
                    return False

        return True
