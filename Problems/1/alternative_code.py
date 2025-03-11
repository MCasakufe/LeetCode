from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair={}
        for i,num  in enumerate(nums):
            if target-num in pair:
                return [i,pair[target-num]]
            pair[num]=i
        pass

            


