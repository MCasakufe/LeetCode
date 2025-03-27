class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dominant_number = self.majorityElement(nums)
        if dominant_number == -1:
            return -1
        dominant_number_counter = 0
        for index, number in enumerate(nums):
            if number == dominant_number:
                dominant_number_counter += 1
            if dominant_number_counter > index + 1 - dominant_number_counter:
                return index if index != len(nums) - 1 else -1
        return -1

    def majorityElement(self, nums):
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1

        count = 0
        for num in nums:
            if num == candidate:
                count += 1
        print(count, len(nums), len(nums) / 2)
        if (count > len(nums) // 2) and count - 2 >= len(nums) - count:
            return candidate
        return -1

          
            
if __name__ == "__main__":
    sol = Solution()
    nums = [2,1,3,1,1,1,7,1,2,1]
    print(sol.majorityElement(nums)) # 2
    print(sol.minimumIndex(nums)) # 
