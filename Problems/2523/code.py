class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_prime(n):
            # Casos básicos
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            # Comenzar la verificación desde 5, comprobando solo los números 6k ± 1
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            return True
        min_distance = float('inf')
        left_prime = 0
        smaller_distance_left_prime = 0
        for i in range(left, right + 1):
            if not left_prime and is_prime(i):
                left_prime = i
            elif is_prime(i):
                ditance_between_primes = i - left_prime
                if ditance_between_primes < min_distance:
                    min_distance = ditance_between_primes
                    smaller_distance_left_prime = left_prime
                if min_distance == 2:
                    return [smaller_distance_left_prime, smaller_distance_left_prime + min_distance]
                left_prime = i
        if min_distance == float('inf'):
            return [-1,-1]
        return [smaller_distance_left_prime, smaller_distance_left_prime + min_distance]
        
if __name__ == '__main__':
    left = 19
    right = 31
    solution = Solution()
    print(solution.closestPrimes(left, right))