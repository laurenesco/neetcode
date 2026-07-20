# Memory: 7.7 MB•Time: 28ms•Submitted at: 07/15/2026 16:06
# Beats 100% in runtime, 97.2% in memory

# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.

# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        max_length = 0
        chars = {}

        for r in range(len(s)):
            chars[s[r]] = chars.get(s[r], 0) + 1
            most_occurences = max(chars.values())

            while (r - l + 1) - most_occurences > k:
                chars[s[l]] -= 1
                l += 1
                most_occurences = max(chars.values())

            max_length = max(max_length, r - l + 1)

        return max_length
