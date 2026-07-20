# Memory: 7.9 MB•Time: 29ms•Submitted at: 07/17/2026 18:14
# Beats 100% in runtime, 80.27% in memory

# Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

# You may assume that the correct output is always unique.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        need_dict = {}
        have_dict = {}
        l, have, length = 0, 0, 0
        result = ''

        # Initialize need_dict
        for c in t:
            need_dict[c] = need_dict.get(c, 0) + 1

        need = len(need_dict)

        # Iterate over have_dict
        for r in range(len(s)):

            # If the char is in t, increment count in have_dict
            if s[r] in need_dict:

                # Increment have_dict count, necessarily
                have_dict[s[r]] = have_dict.get(s[r], 0) + 1

                # Increment have, if necessary
                if need_dict[s[r]] == have_dict[s[r]]:
                    have += 1

                # Save substring, if necessary
                while need == have:
                    if length == 0 or r - l + 1 < length:
                        result = [l, r]
                        length = r - l + 1

                    if s[l] in have_dict:
                        have_dict[s[l]] -= 1
                        if have_dict[s[l]] < need_dict[s[l]]:
                            have -= 1

                    l += 1

        return s[result[0]:result[1] + 1] if result else ''
