class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq_dict = {}
        boolean_array = [False] * 26
        ans = []

        for char in s:
            if freq_dict.get(char) is None:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1

        ans.append(s[0])
        freq_dict[s[0]] -= 1
        boolean_array[ord(s[0]) - ord('a')] = True

        for i in range(1, len(s), 1):
            if boolean_array[ord(s[i]) - ord('a')] is False:
                for j in range(len(ans)-1, -1, -1):
                    if freq_dict.get(ans[j]) == 0 or s[i] > ans[j]:
                        ans.append(s[i])
                        boolean_array[ord(s[i]) - ord('a')] = True
                        freq_dict[s[i]] -= 1
                        break
                    else:
                        boolean_array[ord(ans[j]) - ord('a')] = False
                        ans.pop(j)
                else:
                    ans.append(s[i])
                    boolean_array[ord(s[i]) - ord('a')] = True
                    freq_dict[s[i]] -= 1
            else:
                freq_dict[s[i]] -= 1

        return ''.join(ans)
