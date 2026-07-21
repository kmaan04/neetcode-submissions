class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in sum_map: # use sum map to store diff between target and num
                return [sum_map[diff],index] # if diff in sum_map return in list along with index of num
            sum_map[num] = index 
        