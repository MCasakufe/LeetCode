class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        concatenated_value=0
        right=len(nums)-1
        while left < right:
            concatenated_value += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        if left == right:
            concatenated_value += int(str(nums[left]))
        return concatenated_value