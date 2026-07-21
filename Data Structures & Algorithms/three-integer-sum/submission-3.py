class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]: # check prev neighbour does not have same value
                continue

            if num > 0: # list sorted - cutoff: if n > 0, then n+1, n+2 ... do not add to = 0
                break # breaks out of loop and trasnfers control to code outside loop
            
            l, r = i+1, len(nums) - 1

            while l < r:
                threeSum = num + nums[l] + nums [r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([ num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
        return res
            

