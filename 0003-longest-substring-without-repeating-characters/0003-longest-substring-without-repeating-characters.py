class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_len = 0

        sub_unique = set()

        for r in range(len(s)):
            while (s[r] in sub_unique):
                sub_unique.remove(s[left])
                left += 1

            sub_unique.add(s[r])

            max_len = max(max_len , len(sub_unique))
        
        return max_len
           
