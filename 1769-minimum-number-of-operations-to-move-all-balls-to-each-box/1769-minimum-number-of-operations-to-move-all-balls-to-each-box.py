class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        count = 0
        l = 0
        r = 0
        ans = []
        while l<len(boxes):
            if r == len(boxes):
                ans.append(count)
                l += 1
                r = 0
                count = 0
                continue

            if l!=r and boxes[r]=='1':
                count += abs(r-l)
            
            r += 1
        
        return ans

        
            
            
        