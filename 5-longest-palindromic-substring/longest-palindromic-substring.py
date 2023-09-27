class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        The idea is to first iterate over the string s by one character at a time. And for every single character we will move in
        both the directions i.e. left and right by using two pointers and then compare these two pointer values. We will
        keep on moving the pointers in both directions until characters are matching.
        Now, we will iterate over the string s by two characters at a time. We will move in both the directions i.e. left
        and right by using two pointers and then compare these two pointer values. We will keep on moving the pointers in
        both directions until characters are matching.
        While iterating we will maintain max_length and also the start and end index of the max palindromic substring.
        """
        max_length = 1  # this will store the max length of the palindromic substring
        index1, index2 = 0, 0  # these will store start and end index

        # This for loop iterates one character at a time. This for loop runs from index 1 -> len(s)-1
        for i in range(1, len(s)-1, 1):
            j = i - 1  # j is the pointer which will move to the left
            k = i + 1  # k is the pointer which will move to the right
            while j >= 0 and k < len(s):  # iterate till j >= 0 and k < len(nums)
                if s[j] == s[k]:  # if both the pointer values are same then calculate the length
                    length = k - j + 1  # this is the length of the palindromic substring
                    if length > max_length:  # if length is greater than max_length then store start and end index
                        max_length = length
                        index1 = j  # this is the start index
                        index2 = k  # this is the end index
                else:  # if the pointer values does not match then just break and don't iterate further
                    break
                j -= 1  # keep on decreasing j by 1 if pointer value matches
                k += 1  # keep on increasing k by 1 if pointer value matches

        # This for loop considers two characters at a time. This for loop runs from index 0 -> len(s)-1
        for i in range(0, len(s)-1, 1):
            if s[i] == s[i+1]:  # we will only check for palindromic substring only if s[i]==s[i+1]
                length = 2  # is s[i] == s[i+1] then length will always be 2
                if length > max_length:
                    max_length = length
                    index1 = i  # store start index
                    index2 = i + 1  # store last index
                # below code is same as the above code because the two pointer logic works same
                j = i - 1
                k = i + 2
                while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        length = k - j + 1
                        if length > max_length:
                            max_length = length
                            index1 = j
                            index2 = k
                    else:
                        break
                    j -= 1
                    k += 1

        return s[index1: index2+1]
