class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict_count = {}
        for num in nums:
            if num in dict_count:
                dict_count[num] += 1
            else:
                dict_count[num] = 1
        for key in dict_count:
            if dict_count[key] % 2 != 0:
                return False
        return True
            
            

if __name__ == '__main__':
    candies = [5,8,6]
    k = 3
    solution = Solution()
    print(solution.maximumCandies(candies, k))

            