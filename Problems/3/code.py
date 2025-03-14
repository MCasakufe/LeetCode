class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        max_length = 0
        seen = []
        while right < len(s):
            if s[right] not in seen:
                seen.append(s[right])
                right += 1
                if right - left > max_length:
                    max_length = right - left
            else:
                first_seen = seen.index(s[right])
                seen = seen[first_seen + 1:]
                seen.append(s[right])
                left += first_seen + 1
                right += 1

        return max_length

if __name__ == '__main__':
    s = "pwwkew"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))
    pass
        