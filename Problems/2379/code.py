class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        if len(blocks) < k:
            return 0
        white_count = blocks[:k].count('W')
        min_recolors = white_count
        #print(blocks[:k],white_first_option_count)
        for block_index in range(1, len(blocks)-k+1):
            if blocks[block_index-1] == 'W':
                white_count -= 1
            if blocks[block_index+k-1] == 'W':
                white_count += 1
            min_recolors = min(min_recolors, white_count)
            if min_recolors == 0:
                return 0
        return min_recolors
            
            

if __name__ == '__main__':
    blocks = "BWWWBB"
    k = 5
    solution = Solution()
    print(solution.minimumRecolors(blocks, k))

            