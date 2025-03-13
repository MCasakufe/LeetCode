import numpy as np
class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        This one passed LeetCode
        """
        nums_length = len(nums)
        if all(x == 0 for x in nums):
            return 0
        
        def can_zero(query_count):
            difference_array = [0] * (nums_length + 1)
            for query_index in range(query_count):
                left, right, value = queries[query_index]
                difference_array[left] += value
                if right + 1 < nums_length:
                    difference_array[right + 1] -= value
            current_sum = 0
            for index in range(nums_length):
                current_sum += difference_array[index]
                if current_sum < nums[index]:
                    return False
            return True

        left = 0
        right = len(queries)
        while left < right:
            mid = (left + right) // 2
            if can_zero(mid):
                right = mid
            else:
                left = mid + 1
        return left if can_zero(left) else -1
