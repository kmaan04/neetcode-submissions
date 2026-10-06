class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [] # output array

        prefix = 1 # prefix multiplier - updated by multiplying previous elem
        for i in range(len(nums)):
            if i != 0: # ignore first elem as no previous elem before it
                prefix *= nums[i-1]
            res.append(prefix)

        postfix = 1 # postfix multiplier = updated by multiplying next elem 
        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1: # ignore last elem as no next elem after it
                postfix *= nums[i+1] 
            res[i] *= postfix

        return res