class Solution:
    def interpret(self, command: str) -> str:
        my_dict = {}
        my_dict[ord('G')] = 'G'
        my_dict[ord('(') + ord(')')] = 'o'
        my_dict[ord('(') + ord('a') + ord('l') + ord(')')] = 'al'

        sum = 0
        ans_list = []

        for char in command:
            sum += ord(char)
            if my_dict.get(sum):
                ans_list.append(my_dict.get(sum))
                sum = 0

        return ''.join(ans_list)
