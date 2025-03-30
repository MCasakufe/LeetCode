class Solution(object):
    def maximumScore(self, nums, k):
        MOD = 10**9 + 7
        prime_factor_counts = [self._prime_factor_count(n) for n in nums]
        sorted_nums = sorted([(nums[i], i) for i in range(len(nums))],
                             key=lambda x: x[0],
                             reverse=True)
        score = 1
        operations_so_far = 0
        pivot = 0
        
        while operations_so_far < k and pivot < len(sorted_nums):
            possible_subarrays = min(
                self._possible_subarrays(prime_factor_counts, sorted_nums[pivot][1]),
                k - operations_so_far
            )
            score = (score * pow(sorted_nums[pivot][0], possible_subarrays, MOD)) % MOD
            operations_so_far += possible_subarrays
            pivot += 1
        return score % MOD

    def _prime_factor_count(self, n):
        count = 0
        factor = 2
        while factor * factor <= n:
            if n % factor == 0:
                count += 1
                while n % factor == 0:
                    n //= factor
            factor += 1 if factor == 2 else 2
        if n > 1:
            count += 1
        return count

    def _possible_subarrays(self, prime_factor_counts, index):
        nums_length = len(prime_factor_counts)
        index_prime_val = prime_factor_counts[index]

        left, right = index, index
        while left > 0 and prime_factor_counts[left - 1] < index_prime_val:
            left -= 1
        while right < nums_length - 1 and prime_factor_counts[right + 1] <= index_prime_val:
            right += 1
        return (right - index + 1) * (index - left + 1)
