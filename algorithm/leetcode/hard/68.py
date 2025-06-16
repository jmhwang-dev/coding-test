from typing import List

# TODO: Refactor to be more Pythonic
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        output = []
        target_words = []
        lenght_sum = 0
        for i, word in enumerate(words):
            length_word = len(word)
            if lenght_sum + length_word <= maxWidth:
                lenght_sum += length_word + 1
                target_words.append(word)
                target_words.append(' ')
                continue

            target_words.pop()
            lenght_sum -= 1

            if lenght_sum != maxWidth and i < len(words):
                if len(target_words) == 1:
                    last_words = ' '.join(target_words)
                    last_words += ' ' * (maxWidth - len(last_words))
                    output.append(last_words)
                
                else:
                    index = 1
                    while lenght_sum < maxWidth:
                        target_words[index] += ' '
                        lenght_sum += 1
                        index += 2
                        if index >= len(target_words):
                            index = 1
                    
                    output.append(''.join(target_words))
            else:
                output.append(''.join(target_words))
            
            target_words = [word, ' ']
            lenght_sum = len(word) + 1

        target_words.pop()
        last_words = ''.join(target_words)
        last_words += ' ' * (maxWidth - len(last_words))
        output.append(last_words)
        
        return output

sol = Solution()
output = sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
print(output)