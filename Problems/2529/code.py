class Solution(object):
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = self.negative_binarySearch(nums)
        pos = self.positive_binarySearch(nums)
        print(neg, pos)
        if neg is None and pos is None:
            return 0
        if neg and pos:
            return max(self.negative_binarySearch(nums) + 1, len(nums) - self.positive_binarySearch(nums))
        if neg:
            return self.negative_binarySearch(nums) + 1
        return len(nums) - self.positive_binarySearch(nums)
        
    
    def negative_binarySearch(self, nums):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < 0:
                left = mid + 1
            else:
                right = mid
        if left - 1 < 0 or nums[left - 1] >= 0:
            return None
        return left - 1

    
    def positive_binarySearch(self, nums):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= 0:
                left = mid + 1
            else:
                right = mid
        if nums[left] <= 0:
            return None
        return left 

if __name__ == '__main__':
    nums = [-2, -2, -1]
    s = Solution()
    print(s.maximumCount(nums))
    pass

        