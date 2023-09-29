class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ME = None
        freq = 0

        for i in nums:
            if ME is None or i == ME:
                ME = i
                freq += 1
            elif i != ME:
                freq -= 1
                if freq == 0:
                    ME = None

        return ME
