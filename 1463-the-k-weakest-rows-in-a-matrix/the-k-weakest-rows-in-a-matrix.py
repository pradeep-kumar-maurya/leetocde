class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """
        The idea is to just iterate over the matrix and then find the per array sum and create a frequency hashmap where
        key will be the sum and value will the index but in a list format because multiple arrays in the matrix can have
        same sum. Then we need to sort the freq_fict and then just iterate over the values of the sorted dict. We will
        return once the length of final array is = k.
        """
        final = []
        freq_dict = {}
        for index, data in enumerate(mat):
            sum = 0
            for i in data:
                sum += i
            if freq_dict.get(sum) is None:
                freq_dict[sum] = [index]
            else:
                freq_dict[sum].append(index)
        freq_dict = dict(sorted(freq_dict.items()))
        for data in freq_dict.values():
            for i in data:
                final.append(i)
                if len(final) == k:
                    return final
