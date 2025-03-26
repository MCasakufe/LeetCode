import math

class Solution(object):
    def minOperations(self, grid, x):
        if not self.isPossible(grid, x):
            return -1
        convergent_point = self.findConvergentPoint(grid, x)
        print(convergent_point)
        return self.calculateOperationsCounter(grid, x, convergent_point)

    def isPossible(self, grid, x):
        rest = grid[0][0] % x
        for row in grid:
            for val in row:
                if val % x != rest:
                    return False
        return True

    def findConvergentPoint(self, grid, x):
        all_values = [val for row in grid for val in row]
        all_values.sort()
        mid = len(all_values) // 2
        return all_values[mid] if len(all_values) % 2 else all_values[mid - 1]
            
    def calculateOperationsCounter(self, grid, x, convergent_point):
        counter = 0
        for row in grid:
            for val in row:
                counter += abs(val - convergent_point) // x
        return counter


    
            
if __name__ == "__main__":
    sol = Solution()
    grid = [[2,4],[6,8]]
    x = 2
    print(sol.minOperations(grid, x)) # 4
