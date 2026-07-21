class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums: # runs O(n) time initialize the counts
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        output = []
        for i in range(k):
            num = max(freq, key=freq.get)
            freq.pop(num)
            output.append(num)

        return output

         
        