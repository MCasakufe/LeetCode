class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        x_coords = [[x[0], x[2]] for x in rectangles]
        y_coords = [[x[1], x[3]] for x in rectangles]
        x_coords.sort(key=lambda x: x[0])
        y_coords.sort(key=lambda x: x[0])
        print(self.areTwoCuts(x_coords, n))
        print(self.areTwoCuts(y_coords, n))
        return self.areTwoCuts(x_coords, n) or self.areTwoCuts(y_coords, n)
    
    def areTwoCuts(self, n_coords, n):
        cut_count = 0
        pivot = 0
        for coord in n_coords:
            if coord[0] > 0 and coord[0] >= pivot:
                cut_count += 1      
            if cut_count == 2:
                return True
            pivot = max(coord[1], pivot)
        if pivot < n:
            cut_count += n - pivot 
        return False


            

        pass
            
if __name__ == "__main__":
    sol = Solution()
    n = 4
    rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
    print(sol.checkValidCuts(n, rectangles)) # 
    