# Memory: 8 MB•Time: 29ms•Submitted at: 04/16/2026 15:12
# Beats 99.76% in runtime, 98.99% in memory

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = '';

        # For each string, concatenate with delimiter
        for word in strs:
            result += word
            result += '`'

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        word = '';

        # For each character in encoded string
        for c in s:

            # Split on delimiter
            if c != '`':
                word += c
            else:
                result.append(word)
                word = ''

        return result
