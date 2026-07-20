# Memory: 8 MB•Time: 29ms•Submitted at: 04/16/2026 15:12
# Beats 99.76% in runtime, 98.99% in memory

Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

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
