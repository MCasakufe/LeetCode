class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half - mid1

            if mid1 < m and nums1[mid1] < nums2[mid2 - 1]:
                left = mid1 + 1
            elif mid1 > 0 and nums1[mid1 - 1] > nums2[mid2]:
                right = mid1 - 1
            else:
                if mid1 == 0:
                    max_left = nums2[mid2 - 1]
                elif mid2 == 0:
                    max_left = nums1[mid1 - 1]
                else:
                    max_left = max(nums1[mid1 - 1], nums2[mid2 - 1])

                if (m + n) % 2 == 1:
                    return max_left

                if mid1 == m:
                    min_right = nums2[mid2]
                elif mid2 == n:
                    min_right = nums1[mid1]
                else:
                    min_right = min(nums1[mid1], nums2[mid2])

                return (max_left + min_right) / 2

if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))


