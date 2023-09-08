class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        arr1 = [0] * 26
        arr2 = [0] * 26
        for i in ransomNote:
            arr1[ord(i)-97] += 1
        for i in magazine:
            arr2[ord(i)-97] += 1
        for i in range(len(arr1)):
            if arr1[i] > arr2[i]:
                return False
        return True
