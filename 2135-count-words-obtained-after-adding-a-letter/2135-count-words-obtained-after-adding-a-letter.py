class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def to_bitmask(word):
            mask = 0
            for char in word:
                mask |= (1 << (ord(char) - ord('a')))
            return mask

        startWords_masks = {to_bitmask(word) for word in startWords}
        count = 0

        for word in targetWords:
            target_mask = to_bitmask(word)
            for char in word:
                if target_mask ^ (1 << (ord(char) - ord('a'))) in startWords_masks:
                    count += 1
                    break

        return count