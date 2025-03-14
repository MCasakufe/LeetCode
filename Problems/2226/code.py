class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        if len(candies) == 1:
            return candies[0] // k
        candies.sort(reverse=True)

        low = 1
        high = sum(candies) // k
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if self.can_distribute(candies, k, mid):
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer
    
    def can_distribute(self, candies, k, candies_count):
            current_kids = 0
            if len(candies) > k:
                candies = candies[:k]
            for candy_pile in candies:
                if candy_pile < candies_count:
                    return False
                current_kids += candy_pile // candies_count
                if current_kids >= k:
                    return True
            return False

        
            
            

if __name__ == '__main__':
    candies = [5,8,6]
    k = 3
    solution = Solution()
    print(solution.maximumCandies(candies, k))

            