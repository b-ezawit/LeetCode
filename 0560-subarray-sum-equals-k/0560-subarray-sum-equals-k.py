class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sr = 0
        sum_map = defaultdict(int)
        sum_map[0] = 1
        count = 0

        for i in range(len(nums)):
            sr += nums[i]
            if sr-k in sum_map:
                count += sum_map[sr-k]
            
                
            sum_map[sr] += 1
        return count
        
            




        