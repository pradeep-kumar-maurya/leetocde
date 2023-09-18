class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
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
