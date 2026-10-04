class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for i in range(k):
            largest = max(freq, key=freq.get)
            freq.pop(largest)
            res.append(largest)

        return res
        