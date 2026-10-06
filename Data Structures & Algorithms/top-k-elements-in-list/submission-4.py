class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)] # create as many buckets as possible max freq possible - in max case all numbers same so index from 0 - len(nums)

        for num , count in freq.items(): # .items() returns dict as list of tuples (key, value) -> [(k, v), (k, v) ... ]
            buckets[count].append(num)

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        