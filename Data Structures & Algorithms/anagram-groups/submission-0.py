class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for w in strs:
            word = "".join(sorted(w))
            if word in anagrams:
                anagrams[word].append(w)
            else:
                anagrams[word] = [w]

        return list(anagrams.values())