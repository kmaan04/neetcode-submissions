class Solution:
    def isValid(self, s: str) -> bool:
        bracketPairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        stack = []

        for char in s:
            if char in bracketPairs: # check if char is an opening brace
                stack.append(bracketPairs[char]) # appends all the opeing braces
            else: # if not an opening brace ...
                if not stack or stack.pop() != char:
                    return False
        
        return len(stack) == 0