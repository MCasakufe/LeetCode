class Solution(object):
    def maximumScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        MOD = 10**9 + 7
        score = 1
        operations_so_far = 0
        sorted_nums_pivot = 0
        sorted_nums = sorted([(nums[i], i) for i in range(len(nums))], key=lambda x: x[0], reverse=True)
        print(self.possible_subarrays(nums, sorted_nums[0][1]))
        while operations_so_far < k and sorted_nums_pivot < len(sorted_nums):
            possible_subarrays = min(self.possible_subarrays(nums, sorted_nums[sorted_nums_pivot][1]), k - operations_so_far)
            score *= (sorted_nums[sorted_nums_pivot][0]**possible_subarrays)
            sorted_nums_pivot += 1
            operations_so_far += possible_subarrays
            score %= MOD
        return score % MOD

            


    def SieveEratosthenes(self, number):
        sieve = [True]*(number+1)
        for i in range(2, int(number**0.5)+1):
            if sieve[i]:
                for j in range(i*i, number+1, i):
                    sieve[j] = False
        count = 0
        temp = number
        for i in range(2, number+1):
            if sieve[i] and temp % i == 0:
                count += 1
                while temp % i == 0:
                    temp //= i
            if temp == 1:
                break
        return count

    def possible_subarrays(self, nums, index):
        left = index
        right = index
        index_prime_value = self.SieveEratosthenes(nums[index])
        nums_length = len(nums)
        next_left_prime_value = self.SieveEratosthenes(nums[left-1]) if left > 0 else 0
        next_right_prime_value = self.SieveEratosthenes(nums[right+1]) if right < nums_length - 1 else 0
        while left > 0 and next_left_prime_value < index_prime_value:
            left -= 1
            next_left_prime_value = self.SieveEratosthenes(nums[left-1]) if left > 0 else 0
        while right < nums_length - 1 and next_right_prime_value <= index_prime_value:
            right += 1
            next_right_prime_value = self.SieveEratosthenes(nums[right+1]) if right < nums_length - 1 else 0
        return (right - index + 1)*(index - left + 1)

          
            
if __name__ == "__main__":
    sol = Solution()
    nums = [1,7,11,1,5]
    k = 14
    print(sol.maximumScore(nums, k)) 
