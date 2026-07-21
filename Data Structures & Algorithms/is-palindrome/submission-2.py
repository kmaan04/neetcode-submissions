class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalpha() or char.isdigit()]).lower()
        palindrome = True
        
        i, j = 0, len(s)-1
        
        while i < j:
            first, last = s[i], s[j]
            if first != last:
                return False
                
            i += 1
            j -= 1
            
        
        return palindrome
