class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for s in strs:
            count = [0] * 26
            for l in s:
                count[ord(l) - ord('a')] += 1
            
            k = tuple(count)
            if k in groups:
                groups[k].append(s)
            else:
                groups[k] = [s]
        
        return list(groups.values())


        