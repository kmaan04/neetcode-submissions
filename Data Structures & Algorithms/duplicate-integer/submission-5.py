class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = {}
        for num in nums:
            if num in count_dict:
                return True
            else:
                count_dict[num] = 1
        return False
