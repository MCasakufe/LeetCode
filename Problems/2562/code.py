class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        concatenated_value = 0
        while len(nums) > 0:
            if len(nums) == 1:
                concatenated_value += nums[0]
                return concatenated_value
            concatenated_value += int(str(nums.pop(0))+ str(nums.pop(-1)))
        return concatenated_value


if __name__ == '__main__':
    nums = [5,14,13,8,12]
    s = Solution()
    print(s.findTheArrayConcVal(nums))
    pass

        