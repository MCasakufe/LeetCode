class Solution(object):
    def longestNiceSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 1
        current_len = 1
        index = 1
        further_compatible_index = 0
        while index <= len(nums)-1:
            is_compatible = True
            if further_compatible_index == index:
                index += 1
            else:
                for comparison_index in range(further_compatible_index, index):
                    if not (nums[comparison_index]&nums[index] == 0):
                        is_compatible = False
                        further_compatible_index = comparison_index + 1
                        max_len = max(max_len, current_len)
                        current_len = index - comparison_index
                if is_compatible:
                    current_len += 1
                index += 1
            
        max_len = max(max_len, current_len)
        return max_len
            
            

if __name__ == '__main__':
    nums = [135745088,609245787,16,2048,2097152]
    solution = Solution()
    print(solution.longestNiceSubarray(nums))

            