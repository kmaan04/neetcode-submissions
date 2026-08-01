class Solution:
    def findMin(self, nums: List[int]) -> int:
        # brute force
        minn = nums[0]

        for num in nums:
            minn = min(minn, num)

        return minn
        