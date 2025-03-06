class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        flattened_grid = list()
        for row in grid:
            for num in row:
                flattened_grid.append(num)
        n = len(flattened_grid)
        supossed_total = n*(n+1)//2
        total = sum(flattened_grid)
        for i in range(1, n+1):
            if i not in flattened_grid:
                missing = i
        return [missing + total - supossed_total, missing]

if __name__ == '__main__':
    print(1 in [[9,1,7],[8,9,2],[3,4,6]])
    grid = [[9,1,7],[8,9,2],[3,4,6]]
    s = Solution()
    print(s.findMissingAndRepeatedValues(grid))
