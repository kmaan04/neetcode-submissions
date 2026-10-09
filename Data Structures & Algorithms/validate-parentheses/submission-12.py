class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')' : '(', ']' : '[', '}' : '{'}

        stack = []

        if len(s) % 2 != 0:
            return False
        
        for b in s:
            if b in pairs:
                if stack and stack[-1] == pairs[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0



        

