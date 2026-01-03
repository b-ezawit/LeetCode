class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            output.append(prefix)
            prefix *= nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            output[j] *= postfix
            postfix *= nums[j]

        return output
    
        