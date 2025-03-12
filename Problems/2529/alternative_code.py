import bisect

class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_count = bisect.bisect_left(nums, 0)
        pos_count = len(nums) - bisect.bisect_left(nums, 1)
        return max(neg_count, pos_count)
        