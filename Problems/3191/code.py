class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        for index in range(len(nums)-2):
            if nums[index] == 0:
                nums[index] = 1
                self.changeValue(nums, index + 1)
                self.changeValue(nums, index + 2)
                counter += 1
        if all(nums):
            return counter
        return -1
        

            

    def changeValue(self, nums, index):
        if nums[index] == 1:
            nums[index] = 0
        else:
            nums[index] = 1
