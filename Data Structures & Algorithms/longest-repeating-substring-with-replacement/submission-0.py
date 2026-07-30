class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        freq = {}
        mostfreq = 0
        l = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            windowSize = r + 1 - l
            mostfreq = max(mostfreq, freq[s[r]])
            if windowSize - mostfreq > k:
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
        
        return res

        
        