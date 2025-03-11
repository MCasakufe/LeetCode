class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 1:
            pivot1, pivot2 = 0, 0
            last_added = None
            for _ in range(total_length // 2 + 1):
                if pivot1 < len(nums1) and pivot2 < len(nums2):
                    if nums1[pivot1] < nums2[pivot2]:
                        pivot1 += 1
                        last_added = nums1[pivot1 - 1]
                    else:
                        pivot2 += 1
                        last_added = nums2[pivot2 - 1]
                elif pivot1 < len(nums1):
                    pivot1 += 1
                    last_added = nums1[pivot1 - 1]
                else:
                    pivot2 += 1
                    last_added = nums2[pivot2 - 1]
            return last_added
        else:
            pivot1, pivot2 = 0, 0
            last_added, before_last = None, None
            for _ in range(total_length // 2 + 1):
                before_last = last_added
                if pivot1 < len(nums1) and pivot2 < len(nums2):
                    if nums1[pivot1] < nums2[pivot2]:
                        pivot1 += 1
                        last_added = ("nums1", nums1[pivot1 - 1])
                    else:
                        pivot2 += 1
                        last_added = ("nums2", nums2[pivot2 - 1])
                elif pivot1 < len(nums1):
                    pivot1 += 1
                    last_added = ("nums1", nums1[pivot1 - 1])
                else:
                    pivot2 += 1
                    last_added = ("nums2", nums2[pivot2 - 1])
            return (last_added[1] + before_last[1]) / 2.0


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3]
    print(solution.findMedianSortedArrays(nums1, nums2))
    pass