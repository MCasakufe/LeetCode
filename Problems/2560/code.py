class Solution(object):
    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indexed_sorted_nums = sorted(enumerate(nums), key=lambda x: x[1]) #[(index, value)]
        stolen_houses = [False]*len(nums)
        max_value = 0
        for index, val in indexed_sorted_nums:
            print(index, val)
            if self.can_be_stolen(index, k, stolen_houses):
                stolen_houses[index] = True
                if nums[index] > max_value:
                    max_value = nums[index]
            
            if sum(stolen_houses) == k:
                break
        return None

        return max(stolen_houses_quantity)

    def can_be_stolen(self, index, k, stolen_houses):
        if len(stolen_houses) == 1:
            return True
        if len(stolen_houses) < index + 1:
            if not stolen_houses[index - 1]:
                return True
        if index == 0:
            if not stolen_houses[index + 1]:
                return True
        if not stolen_houses[index- 1] and not stolen_houses[index + 1]:
            return True
        return False

        pass




            
        

if __name__ == '__main__':
    nums = [2,3,5,9]
    k = 2
    s = Solution()
    print(s.minCapability(nums, k))

    pass

        