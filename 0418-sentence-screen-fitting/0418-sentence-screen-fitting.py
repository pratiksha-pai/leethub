class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        s = ' '.join(sentence) + ' '
        start = 0
        length = len(s)
        for i in range(rows):
            start += cols
            if s[start % length] == ' ':
                start += 1
            else:
                while start > 0 and s[(start-1) % length] != ' ':
                    start -= 1
        return start // length