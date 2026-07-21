class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        prefix = 1
        for i in range(len(nums)):
            if i != 0:
                prefix = prefix * nums[i-1]
            output.append(prefix)
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            if i != len(nums)-1:
                postfix = postfix * nums[i+1]
            output[i] = output[i] * postfix    
        
        return output
        


        
        