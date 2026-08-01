class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            midIndex = (left+right) // 2

            if nums[midIndex] == target:
                return midIndex

            if nums[left] <= nums[midIndex]: # left half of array sorted
                if nums[left] <= target < nums[midIndex]: # is the target in left half
                    right = midIndex - 1 # target in left sub array
                else:
                    left = midIndex + 1 # target in right
            else: # right half of array sorted 
                if nums[midIndex] < target <= nums[right]: # is target in right half
                    left =  midIndex + 1         
                else: # is target in  left half
                    right = midIndex - 1

        return -1

