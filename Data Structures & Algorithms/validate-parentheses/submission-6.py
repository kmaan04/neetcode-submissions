class Solution:
    def isValid(self, s: str) -> bool:
        matches = {'(' : ')', '{' : '}', '[' :  ']' }

        if len(s) % 2 != 0:
            return False
        
        stack = []

        for char in s:
            if char in matches:
                stack.append(matches[char])
            else:
                if not stack or stack.pop() != char:
                    return False
        
        return len(stack) == 0

        