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
                stack.append(char)
            else:
                if stack and bracketPairs[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
                    
        return len(stack) == 0

                
        
        