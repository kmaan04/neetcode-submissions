class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            histogram = [0] * 26
            for l in s:
                letter_index = ord(l) - ord('a') # find offset from a
                histogram[letter_index] += 1

            k = tuple(histogram)
            anagrams[k].append(s)

        return list(anagrams.values())

        