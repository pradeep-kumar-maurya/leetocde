class Solution:
    def manipulate_text(self, length, maxWidth, temp, output):
        if len(temp) == 1:
            output.append(temp[0] + " " * (maxWidth - length))
            return

        total_spaces = maxWidth - length
        empty_place = len(temp) - 1
        string = ""

        for i, word in enumerate(temp):
            if i == len(temp) - 1:
                break
            if total_spaces % empty_place:
                spaces_to_add = (total_spaces // empty_place) + 1
            else:
                spaces_to_add = total_spaces // empty_place

            string += (word + " " * spaces_to_add)
            total_spaces -= spaces_to_add
            empty_place -= 1

        string += temp[-1]
        output.append(string)

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        temp = []
        length = 0

        for word in words:
            length += len(word) + 1  # length of the word + 1 space after the word
            if length <= maxWidth:
                temp.append(word)
            elif length - 1 == maxWidth:
                temp.append(word)
                length = length - 1 - (len(temp) - 1)
                self.manipulate_text(length, maxWidth, temp, output)
                length = 0
                temp = []
            elif length > maxWidth:
                length -= len(word) + 1 + len(temp)
                self.manipulate_text(length, maxWidth, temp, output)
                length = 0
                length += len(word) + 1
                temp = []
                temp.append(word)
        else:
            if len(temp) > 0:
                output.append(" ".join(temp))
                output[-1] = output[-1] + " " * (maxWidth - len(output[-1]))

        return output
