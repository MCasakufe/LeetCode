class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        start = 0
        used_bits = 0
        for i in range(len(nums)):
            while used_bits & nums[i]:
                used_bits ^= nums[start]
                start += 1
            used_bits |= nums[i]
            max_len = max(max_len, i - start + 1)
        return max_len

