class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = 0
        for i in nums:
            XOR = XOR ^ i
        return XOR