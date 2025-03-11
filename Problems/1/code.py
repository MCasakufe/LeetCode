class Solution:
    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        return self.merge(left, right)


    def twoSum(self, nums, target: int):
        merged = self.merge_sort(nums)
        print(merged)
        left = 0
        right = len(merged) - 1
        sum = merged[left] + merged[right]
        while sum != target:
            if sum < target:
                left += 1
            else:
                right -= 1
            sum = merged[left] + merged[right]
        idx_left = nums.index(merged[left])
        if merged[left] == merged[right]:
            idx_right = nums.index(merged[right], idx_left + 1)
        else:
            idx_right = nums.index(merged[right])
        return [idx_left, idx_right]
    
if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,4]
    target = 6
    print(f"Input: nums = {nums}, target = {target}")
    result = solution.twoSum(nums, target)
    print(f"Output: {result}")
