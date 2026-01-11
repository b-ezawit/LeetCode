class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        nums1[:] = nums1[:m]
        nums1.sort()
        nums2.sort()

        l = 0
        r = 0

        while l<m and r<n:
            if nums2[r] <= nums1[l]:
                nums1.insert(l,nums2[r])
                r += 1
            else:
                l += 1
        
        while r<n:
            nums1.append(nums2[r])
            r += 1
        nums1.sort()
        return nums1

