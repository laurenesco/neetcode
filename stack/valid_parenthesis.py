# Memory: 7.7 MB•Time: 27ms•Submitted at: 05/11/2026 14:36
# Beats 94.84% in runtime, 99.72% in memory

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [];

        for c in s:
            if c in ['[', '{', '(']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False;

                curr = stack.pop()

                if c == ']' and curr != '[':
                    return False

                elif c == '}' and curr != '{':
                    return False 

                elif c == ')' and curr != '(':
                    return False 
                    
        return len(stack) == 0
