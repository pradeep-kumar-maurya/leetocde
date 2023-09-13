class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        The idea is to use a freq_array of size 26 because the string contains only lower case alphabets.
        After creating the freq_array per string, we need to check in the freq_dict as a tuple(freq_arr).
        Overall T.C = O(N*M)
        """
        freq_dict = {}
        for string in strs:  # O(N)
            freq_arr = [0] * 26  # a .... z -> 0 ... 25
            for char in string:  # O(M) where M is the length of the string. Max M could be 100 in this case.
                freq_arr[ord(char) - ord("a")] += 1
            if freq_dict.get(tuple(freq_arr)) is None:
                freq_dict[tuple(freq_arr)] = [string]
            else:
                freq_dict[tuple(freq_arr)].append(string)
        return freq_dict.values()

    """
    This approach uses sorting the string
    def solve(strs):
        '''
        The idea is just to sort the strings in strs array and check in the freq dict.
        I guess overall T.C = O(N^2 logN)
        '''
        freq_dict = {}
        for string in strs:  # O(N)
            sorted_str = "".join(sorted(string))  # O(NlogN)
            if freq_dict.get(sorted_str) is None:
                freq_dict[sorted_str] = [string]
            else:
                freq_dict[sorted_str].append(string)
        return freq_dict.values()
    """
