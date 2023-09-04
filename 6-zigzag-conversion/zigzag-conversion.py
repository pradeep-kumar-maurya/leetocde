class Solution:
    def convert(self, s: str, n: int) -> str:
        
        result = ""
        k = 0
        toggle = 0

        if n == 1:
            return s

        while k < n:
            temp = [((n-1) - k) * 2, (k - 0) * 2]
            i = k
            while i < len(s):
                result += s[i]
                if k == 0:
                    i += temp[0]
                elif k == n - 1:
                    i += temp[1]
                else:
                    i += temp[toggle]
                    toggle = toggle ^ 1
            k += 1
            toggle = 0

        return result
        