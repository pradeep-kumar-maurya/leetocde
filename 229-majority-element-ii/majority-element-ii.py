class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ME1, freq1 = None, 0
        ME2, freq2 = None, 0
        ans = []

        for i in nums:
            if i == ME1:
                ME1 = i
                freq1 += 1
            elif i == ME2:
                ME2 = i
                freq2 += 1
            elif ME1 is None:
                ME1 = i
                freq1 += 1
            elif ME2 is None:
                ME2 = i
                freq2 += 1
            elif ME1 is not None and ME2 is not None:
                freq1 -= 1
                freq2 -= 1
                if freq1 == 0:
                    ME1 = None
                if freq2 == 0:
                    ME2 = None

        ME1_count, ME2_count = 0, 0
        for i in nums:
            if i == ME1:
                ME1_count += 1
            elif i == ME2:
                ME2_count += 1

        if ME1_count > (len(nums) // 3):
            ans.append(ME1)
        if ME2_count > (len(nums) // 3):
            ans.append(ME2)

        return ans
