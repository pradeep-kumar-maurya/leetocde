class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        The idea is to use an array like a stack. We will add character to the stack one by one depending on a few conditions
        and also decrement the count of that character in the frequency hashmap. At the same time we will mark the added
        character to True in the boolean array.
        If the character being added is smaller than characters in stack then we will pop the characters from the stack.
        But we will only remove the character from the stack if the count of that character in the frequency hashmap is > 0.
        Also, when we remove characters from stack we will mark that character to False in the boolean array.
        We will use a boolean array as it will help us know if a character was already added in the stack.
        """
        freq_dict = {}  # frequency hashmap
        boolean_array = [False] * 26  # this is the boolean array
        ans = []  # this will behave as a stack

        for char in s:  # first we will prepare a frequency hashmap
            if freq_dict.get(char) is None:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1

        ans.append(s[0])  # before starting anything just append s[0] to ans stack as it would be easy for us further
        # as soon as we add any character to ans stack we need to decrement the count of that character by 1 in the frequency hashmap
        freq_dict[s[0]] -= 1
        boolean_array[ord(s[0]) - ord('a')] = True  # then mark that character to True in the boolean array

        # now iterate from index 1 -> len(s)-1
        for i in range(1, len(s), 1):
            # we will only consider the characters that are False in boolean array
            if boolean_array[ord(s[i]) - ord('a')] is False:
                # first step is to check characters in stack one by one
                for j in range(len(ans)-1, -1, -1):
                    # if the character count from stack is 0 in the frequency hashmap or s[i] > ans[j] then we simply add
                    # s[i] to ans stack because we can't remove a character with count 0 as it would not appear in the future.
                    if freq_dict.get(ans[j]) == 0 or s[i] > ans[j]:
                        ans.append(s[i])  # add s[i] to ans stack
                        boolean_array[ord(s[i]) - ord('a')] = True  # mark s[i] to True in boolean array
                        freq_dict[s[i]] -= 1  # reduce the frequency of s[i] by 1 in the frequency hashmap
                        break  # we should not iterate further in stack
                    else:
                        # else we need to pop character from the ans stack and mark ans[j] to False in the boolean array
                        boolean_array[ord(ans[j]) - ord('a')] = False
                        ans.pop(j)
                # if there was no break from the above for loop then we would have removed all the elements from the stack
                # therefore add s[i] to the ans stack, mark s[i] to True in boolean array and decrement s[i] by 1 in freq_dict.
                else:
                    ans.append(s[i])
                    boolean_array[ord(s[i]) - ord('a')] = True
                    freq_dict[s[i]] -= 1
            else:  # if s[i] is True in the boolean array then just decrement s[i] by 1 in freq_dict
                freq_dict[s[i]] -= 1

        # at last ans stack will have all the unique characters and lexicographically ordered
        return ''.join(ans)
