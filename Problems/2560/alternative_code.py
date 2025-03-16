class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        low, high = min(nums), max(nums)
        while low < high:
            mid_capability = (low + high) // 2
            robbed_count, index = 0, 0
            while index < len(nums):
                if nums[index] <= mid_capability:
                    robbed_count += 1
                    index += 2
                else:
                    index += 1
            if robbed_count >= k:
                high = mid_capability
            else:
                low = mid_capability + 1
        return low