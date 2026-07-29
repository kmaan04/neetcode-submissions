class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):          # fix 1: include last index
            unique = set()
            for j in range(i, len(s)):
                if s[j] in unique:
                    break                  # fix 3: stop this inner loop
                unique.add(s[j])           # fix 2: actually grow the set
                res = max(res, len(unique))
            # fix 4 is handled naturally now, since res updates every step
        return res