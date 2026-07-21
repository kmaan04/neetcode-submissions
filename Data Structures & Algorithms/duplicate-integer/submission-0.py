class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe_hash = {}
        for num in nums:
            if num in dupe_hash:
                return True
            else:
                dupe_hash[num] = 1
        return False
         