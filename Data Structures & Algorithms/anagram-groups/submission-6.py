class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {} # each word is sorted based on whether another word has the same letters / anagram grouping

        for word in strs: # go through each word
            histogram = [0] * 26 # create a freq count of each letter in the selected word as a key for the grouping
            for letter in word:
                histogram[ord(letter) - ord('a')] += 1 # subtract ascii val of a to find  index 0 - 25 of letter in alphabet
            
            key = tuple(histogram)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
            
        return list(groups.values())




        