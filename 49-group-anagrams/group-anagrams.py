class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The idea is just to sort the strings in strs array and check in the freq dict.
        I guess overall T.C = O(N^2 logN)
        """
        freq_dict = {}
        final_array = []
        for string in strs:  # O(N)
            sorted_str = "".join(sorted(string))  # O(NlogN)
            if freq_dict.get(sorted_str) is None:
                freq_dict[sorted_str] = [string]
            else:
                freq_dict[sorted_str].append(string)
        for value in freq_dict.values():
            final_array.append(value)
        return final_array
