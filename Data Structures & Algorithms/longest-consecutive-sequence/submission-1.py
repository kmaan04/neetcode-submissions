class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:

            # check if beginning of a sequence 
            if (num - 1) not in num_set:
                # init length of curr seq.
                length = 1
                # do a set membership to for curr seq until end of seq
                while num + length in num_set:
                    length += 1
                # find longest seq and store it 
                longest = max(longest,  length)
        
        return longest