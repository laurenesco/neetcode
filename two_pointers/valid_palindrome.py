# Memory: 7.6 MB•Time: 27ms•Submitted at: 04/24/2026 14:58
# Beats 93.99% in runtime, 100% in memory

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Clean the input
        s = re.sub(r'[^a-zA-Z0-9]', '', s) 
        
        if s.lower() == s[::-1].lower():
            return True

        return False
        
