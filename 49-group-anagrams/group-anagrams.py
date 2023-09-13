class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_dict = {}
        for string in strs:  # O(N)
            sorted_str = "".join(sorted(string))  # O(NlogN)
            if freq_dict.get(sorted_str) is None:
                freq_dict[sorted_str] = [string]
            else:
                freq_dict[sorted_str].append(string)
        return freq_dict.values()

