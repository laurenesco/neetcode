# Memory: 8.7 MB•Time: 36ms•Submitted at: 04/09/2026 13:23
# Beats 72.51% in runtime, 23.50% in memory

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach: Sort the provided strings, compare the 
        # sorted versions, if matching return true

        return sorted(s) == sorted(t)
