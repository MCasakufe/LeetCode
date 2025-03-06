class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        num_count = [0] * (n * n + 1)
        print(num_count)
        
        for row in grid:
            for num in row:
                num_count[num] += 1
        
        repeated = missing = -1
        for i in range(1, n * n + 1):
            if num_count[i] == 2:
                repeated = i
            elif num_count[i] == 0:
                missing = i
        
        return [repeated, missing]
    
if __name__ == '__main__':
    print(1 in [[9,1,7],[8,9,2],[3,4,6]])
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    s = Solution()
    print(s.findMissingAndRepeatedValues(grid))