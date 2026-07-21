class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears.
        # e.g. nums = [1,1,1,2,2,3] -> count = {1: 3, 2: 2, 3: 1}
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # Step 2: Bucket sort by frequency.
        # freq[i] will hold a list of all numbers that appear exactly i times.
        # Max possible frequency is len(nums), so we need indices 0..len(nums).
        freq = [[] for i in range(len(nums) + 1)]
        for num, cnt in count.items():
            freq[cnt].append(num)
        # e.g. freq = [[], [3], [2], [1], [], [], []]
        #       index:  0    1    2    3   4   5   6

        # Step 3: Walk buckets from highest frequency to lowest,
        # collecting numbers until we have k of them.
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res  # stop as soon as we have k elements

         
        